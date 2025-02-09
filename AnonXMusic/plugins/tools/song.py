import os
import asyncio
import aiohttp
import logging
from pySmartDL import SmartDL
from pyrogram import Client, filters
from youtube_search import YoutubeSearch
from YukkiMusic import app
from strings.filters import command
from mutagen.mp4 import MP4, MP4Cover

logging.basicConfig(level=logging.INFO)

API_KEY = "3ec1818f-f3bc-4da2-a259-48ae227d5955"  # مفتاح API الخارجي
DOWNLOADS_PATH = "downloads"

if not os.path.exists(DOWNLOADS_PATH):
    os.makedirs(DOWNLOADS_PATH)

async def fetch_youtube_data(video_id):
    """استخراج بيانات الفيديو بما في ذلك روابط الصوت والفيديو وصورة الغلاف."""
    api_url = f"https://youtube.virs.tech/vi/{video_id}?key={API_KEY}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status != 200:
                return None
            return await response.json()

async def download_file(url, output_path):
    """تحميل ملف باستخدام SmartDL."""
    try:
        file = SmartDL(url, output_path, progress_bar=False)
        file.start(blocking=False)

        while not file.isFinished():
            await asyncio.sleep(0.5)

        if not os.path.exists(output_path) or os.path.getsize(output_path) == 0:
            return None

        return output_path
    except Exception as e:
        logging.error(f"فشل التحميل: {e}")
        return None

async def download_thumbnail(url, output_path):
    """تحميل صورة الغلاف من YouTube."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    with open(output_path, "wb") as f:
                        f.write(await response.read())
                    return output_path
    except Exception as e:
        logging.error(f"فشل تحميل الصورة: {e}")
    return None

async def download_youtube_audio(video_id):
    """تنزيل الصوت من YouTube مع صورة الغلاف."""
    data = await fetch_youtube_data(video_id)
    if not data:
        return None, None, None

    title = data.get("title", "Audio")
    thumbnail_url = data.get("thumbnail")
    audio_url = None

    for item in data.get("streaming_data", []):
        if item.get("width") == 0 and item.get("height") == 0:
            audio_url = item.get("url")
            break

    if not audio_url:
        return None, None, None

    audio_file = f"{DOWNLOADS_PATH}/{video_id}.m4a"
    file_path = await download_file(audio_url, audio_file)

    thumbnail_path = f"{DOWNLOADS_PATH}/{video_id}.jpg"
    if thumbnail_url:
        thumbnail_path = await download_thumbnail(thumbnail_url, thumbnail_path)

    return file_path, title, thumbnail_path

async def download_youtube_video(video_id):
    """تنزيل الفيديو من YouTube."""
    data = await fetch_youtube_data(video_id)
    if not data:
        return None, None, None

    title = data.get("title", "Video")
    thumbnail_url = data.get("thumbnail")
    video_url = None

    for item in data.get("streaming_data", []):
        if item.get("width") > 0 and item.get("height") > 0:
            video_url = item.get("url")
            break

    if not video_url:
        return None, None, None

    video_file = f"{DOWNLOADS_PATH}/{video_id}.mp4"
    file_path = await download_file(video_url, video_file)

    thumbnail_path = f"{DOWNLOADS_PATH}/{video_id}.jpg"
    if thumbnail_url:
        thumbnail_path = await download_thumbnail(thumbnail_url, thumbnail_path)

    return file_path, title, thumbnail_path

def embed_metadata(audio_path, title, thumbnail_path):
    """إضافة صورة الغلاف واسم الأغنية إلى الملف الصوتي."""
    try:
        audio = MP4(audio_path)
        audio["\xa9nam"] = title  # اسم الأغنية

        # إضافة صورة الغلاف إذا كانت موجودة
        if thumbnail_path and os.path.exists(thumbnail_path):
            with open(thumbnail_path, "rb") as f:
                audio["covr"] = [MP4Cover(f.read(), imageformat=MP4Cover.FORMAT_JPEG)]
        audio.save()
    except Exception as e:
        logging.error(f"فشل تضمين البيانات الوصفية: {e}")

def extract_video_id(query):
    """استخراج معرف الفيديو من الرابط أو البحث عن اسم الفيديو."""
    if "youtube.com" in query or "youtu.be" in query:
        if "watch?v=" in query:
            return query.split("watch?v=")[-1].split("&")[0]
        else:
            return query.split("/")[-1].split("?")[0]
    else:
        try:
            results = YoutubeSearch(query, max_results=1).to_dict()
            return results[0]["id"]
        except Exception:
            return None

@app.on_message(command(["يوت"]) & (filters.private | filters.group | filters.channel))
async def song(client, message):
    query = " ".join(message.command[1:])
    m = await message.reply("⦗ جارٍ البحث ... ⦘")

    video_id = extract_video_id(query)
    if not video_id:
        await m.edit("🚫 **خطأ:** لم يتم العثور على الأغنية.")
        return

    await m.edit("⦗ جارٍ التحميل ... ⦘")

    audio_file, title, thumbnail_path = await download_youtube_audio(video_id)

    if audio_file:
        embed_metadata(audio_file, title, thumbnail_path)

        # إرسال الملف الصوتي مع صورة الغلاف واسم الأغنية
        await message.reply_audio(audio_file, caption=f"- 🎵 {title}", performer="YouTube", thumb=thumbnail_path if os.path.exists(thumbnail_path) else None)

        await m.delete()
        os.remove(audio_file)
    else:
        await m.edit("🚫 **خطأ:** فشل تحميل الصوت.")

@app.on_message(command(["نزلي فيديو"]) & (filters.private | filters.group | filters.channel))
async def video(client, message):
    query = " ".join(message.command[2:])
    m = await message.reply("⦗ جارٍ البحث ... ⦘")

    video_id = extract_video_id(query)
    if not video_id:
        await m.edit("🚫 **خطأ:** لم يتم العثور على الفيديو.")
        return

    await m.edit("⦗ جارٍ التحميل ... ⦘")

    video_file, title, thumbnail_path = await download_youtube_video(video_id)

    if video_file:
        await message.reply_video(video_file, caption=f"- 🎥 {title}")
        await m.delete()
        os.remove(video_file)
    else:
        await m.edit("🚫 **خطأ:** فشل تحميل الفيديو.")
