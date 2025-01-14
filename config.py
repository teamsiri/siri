import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# احصل على هذه القيمة من my.telegram.org/apps
API_ID = int(getenv("API_ID",""))
API_HASH = getenv("API_HASH","")

# احصل على الرمز الخاص بك من @BotFather على Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","")

# احصل على عنوان URL الخاص بـ Mongo من cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 480))

# معرف الدردشة لمجموعة لتسجيل أنشطة الروبوت
LOGGER_ID = int(getenv("LOGGER_ID",'-1001842275903'))

# احصل على هذه القيمة من @FallenxBot على Telegram بواسطة /id
OWNER_ID = int(getenv("OWNER_ID", 5277936711))
OWNER = int(getenv("OWNER", 5277936711))

# اسم تطبيق heroku الخاص بك
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# api heroku الخاص بك
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/teamsiri/siri",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # املأ هذا المتغير إذا كان مستودعك الأصلي خاصًا

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/SourceSiri")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/SourceSiri")

# اضبط هذا على "صحيح" إذا كنت تريد أن يترك المساعد المحادثات تلقائيًا بعد فترة زمنية محددة
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT","")

CHANNEL_SUDO = getenv(
    "CHANNEL_SUDO", "SourceSiri"
)  # معرف قناتك بدون @
YAFA_NAME = getenv(
    "YAFA_NAME", ". Source Siri ."
)  # اسم قناتك
YAFA_CHANNEL = getenv(
   " YAFA_CHANNEL", "https://t.me/SourceSiri"
) 

SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/SourceSiri"
)

BOT_USERNAME = getenv(
    "BOT_USERNAME", "zr3bot"
)

# احصل على هذه البيانات من https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# الحد الأقصى لجلب مسار قائمة التشغيل من روابط youtube وspotify وapple.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999"))

# حد حجم ملفات الصوت والفيديو في Telegram (بالبايت)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# احصل على جلسة Pyrogram v2 الخاصة بك من @StringFatherBot على Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/220034b1e9af0ee930981.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://telegra.ph/file/220034b1e9af0ee930981.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
