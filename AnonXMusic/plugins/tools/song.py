import os
import glob
import random
import requests
import yt_dlp
import wget,asyncio
import logging
from pyrogram import filters
from strings.filters import command
from youtube_search import YoutubeSearch
from AnonXMusic import app
from requests import get,post

import requests
from bs4 import BeautifulSoup
import re

def Convert(Title,Id,Url):
  response = requests.post("https://yt5s.biz/mates/en/convert", params = {
  'id':Id}, data = {
  'platform': "youtube",
  'url':Url,'title': Title,'id': Id,'ext': "mp3",'note': "128k",'format': ""}, headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",'Accept': "application/json, text/javascript, */*; q=0.01",'sec-ch-ua-platform': "\"Android\"",'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",'sec-ch-ua-mobile': "?1",'x-requested-with': "XMLHttpRequest",'x-note': "128k",'origin': "https://yt5s.biz",'sec-fetch-site': "same-origin",'sec-fetch-mode': "cors",'sec-fetch-dest': "empty",'referer': "https://yt5s.biz/ar/",'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",'priority': "u=1, i",'Cookie': "_ga=GA1.1.554701799.1733604582; _ga_VVBEPYMKP2=GS1.1.1733611096.2.0.1733611105.0.0.0"})
  Url = response.json()['downloadUrlX']
  return Url,Title

def Get_ID(URL):
    response = requests.post("https://yt5s.biz/mates/en/analyze/ajax", params={'retry': "undefined",'platform': "youtube",'mhash': None}, data={'url':URL ,'ajax': "1",'lang': "ar"
}, headers={'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",'Accept': "application/json, text/javascript, */*; q=0.01",'sec-ch-ua-platform': "\"Android\"",'x-requested-with': "XMLHttpRequest",'sec-ch-ua': "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    'sec-ch-ua-mobile': "?1",
    'origin': "https://yt5s.biz",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://yt5s.biz/ar/",
    'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",'priority': "u=1, i",'Cookie': "_ga=GA1.1.554701799.1733604582; _ga_VVBEPYMKP2=GS1.1.1733604581.1.0.1733604590.0.0.0"})
    data = response.json()['result']
    soup = BeautifulSoup(data, 'html.parser')
    button = soup.find('button', class_='btn-success')

    if button:
        onclick_value = button['onclick']
        matches = re.findall(r"'(.*?)'", onclick_value)
        if len(matches) >= 2:
            stereo_love = matches[1]
            another_value = matches[2]
            Title = stereo_love
            Id_Video =another_value
            return Convert(Title,Id_Video,URL)



def get_res(video_id):
    
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar,en-GB;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,en-US;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://yt1d.com',
    'priority': 'u=1, i',
    'referer': 'https://yt1d.com/en11/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    }  
      
    # البيانات
    data = {
        'url': f'https://youtu.be/watch?v={video_id}',
        'ajax': '1',
        'lang': 'en',
    }

    # الطلب

    response = requests.post('https://yt1d.com/mates/en/analyze/ajax', headers=headers, data=data)

    # تحليل الرد JSON
    response_json = response.json()
    html_content = response_json.get('result', '')
    # print(html_content)

    # استخدام BeautifulSoup لتحليل الكود HTML المستخرج
    soup = BeautifulSoup(html_content, 'html.parser')

    # البحث عن الأزرار باستخدام الصنف المحدد
    tables = soup.find('table', class_='table table-bordered table-hover table-responsive-sm')
    # print(tables.td)

    # استخراج قيم onclick وتحويلها إلى قاموس باستخدام التعبيرات العادية
    downloads = []
    
    resolutions = set()  # استخدام مجموعة للتأكد من الفريدات
    
    if tables:
        td_elements = tables.find_all('td')
        for td in td_elements:
            text = td.get_text(strip=True)
            if 'p60' in text or '360p' in text or '(.mp4)' in text:
                resolutions.add(text)
    
    # تحويل المجموعة إلى قائمة مع عرض النتائج
    data = [{'resolution': res} for res in resolutions]
    
    return data

def send_request(video_id,res):
    
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en-GB;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,en-US;q=0.5',
        'origin': 'https://loader.to',
        'priority': 'u=1, i',
        'referer': 'https://loader.to/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    params = {
        'start': '1',
        'end': '1',
        'format': res,
        'url': f'https://www.youtube.com/watch?v={video_id}',
    }

    response = requests.get('https://ab.cococococ.com/ajax/download.php', params=params, headers=headers)
    return response.json()

def get_progress(id):

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar,en-GB;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,en-US;q=0.5',
        'origin': 'https://loader.to',
        'priority': 'u=1, i',
        'referer': 'https://loader.to/',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    }

    params = {
        'id': id,
    }

    response = requests.get('https://p.oceansaver.in/ajax/progress.php', params=params, headers=headers)
    return response.json()
def get_bytes(url):
    bytees = requests.get(url).content
    return bytees



def get_cookies_file():
    folder_path = f"{os.getcwd()}/cookies"
    txt_files = glob.glob(os.path.join(folder_path, '*.txt'))
    if not txt_files:
        raise FileNotFoundError("No .txt files found in the specified folder.")
    cookie_txt_file = random.choice(txt_files)
    return cookie_txt_file
def download_audio_and_thumbnail(link):
    try:
        thumbnail_url = "https://k.top4top.io/p_3263gt4va1.jpg"
        if thumbnail_url:
                
                    thumb_file = wget.download(thumbnail_url)
        else:
                thumb_file = None
        Link ,Title  =  Get_ID(link)
        Do = requests.get(Link)
        if os.path.exists(f"downloads/{Title}.mp3") == True:
            return f"downloads/{Title}.mp3",thumb_file,Title
            
        with open(f"downloads/{Title}.mp3",'wb') as D:
            D.write(Do.content)
        return f"downloads/{Title}.mp3",thumb_file,Title
    except Exception as e:
        print("New : "+e)
        
        id = send_request(link.split('v=')[1],360)['id'] 
        while True:
            progress = get_progress(id)
            if progress['text'] == 'Finished': 
                print(progress['download_url'])
                Do = requests.get(progress['download_url'])
                break
        thumbnail_url = "https://k.top4top.io/p_3262rs3261.jpg"      
        if thumbnail_url:
                
                    thumb_file = wget.download(thumbnail_url)
        else:
                thumb_file = None
        Title =  link.split('v=')[1]
        if os.path.exists(f"downloads/{link.split('v=')[1]}.mp3") == True:
            return f"downloads/{link.split('v=')[1]}.mp3",thumb_file,Title                
        with open(f"downloads/{link.split('v=')[1]}.mp3",'wb') as D:
            D.write(Do.content)
        
        
        return f"downloads/{link.split('v=')[1]}.mp3", thumb_file,Title


@app.on_message(command(["/song", "بحث", "تحميل", "تنزيل", "يوت", "yt"]))
async def song(client, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    chutiya = message.from_user.mention

    query = " ".join(message.command[1:])
    
    
    m = await message.reply("جاري البحث يرجى الأنتضار ...")
    results = YoutubeSearch(query, max_results=1).to_dict()
    link = f"https://youtube.com{results[0]['url_suffix']}"
    title = results[0]["title"][:40]
    thumbnail = results[0]["thumbnails"][0]
    thumb_name = f"thumb{title}.jpg"
    loop = asyncio.get_event_loop()
    audio_file, thumb_file,Title = await loop.run_in_executor(None, download_audio_and_thumbnail, link)
    
    try:
        
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)

    except Exception as e:
        await m.edit("لم يتم العثور على الأغنية، يرجى المحاولة مرة أخرى .")
        logging.error(f"Failed to fetch YouTube video: {str(e)}")
        return
    
    await m.edit("جارٍ التنزيل... الرجاء الانتظار ...")
    
    try:
        
            
            rep = f"الاسم: {title[:25]}\nبواسطة: {chutiya}"
            await message.reply_audio(
            audio_file,
            caption=rep,
            performer="@rzzrzz .",
            thumb=thumb_name,
            title=title,
        )
            await m.delete()
    
    except Exception as e:
        await m.edit(f"[Victorious] **\n\**خطأ :** {e}")
        logging.error(f"Error while downloading audio: {str(e)}")

    finally:
        try:
            os.remove(audio_file)
            os.remove(thumb_name)
        except Exception as e:
            logging.error(f"Failed to delete temporary files: {str(e)}")
