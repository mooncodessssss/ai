import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","23468511"))
API_HASH = getenv("API_HASH","872d60743ce5f247a2c0a9e7fac17e1f")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","7838954898:AAEiFQbQeQJPxu6svm_nF7fqgdYVW2W8JVo")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://moon:moon@moon.r2zqa.mongodb.net/?retryWrites=true&w=majority&appName=moon")

# Vars For API End Pont.
YTPROXY_URL = getenv("YTPROXY_URL", 'https://yt.okflix.top/api') ## E.G https://yt.okflix.top/api/jADTdg-o8i0 Returns Download Info.
COOKIES_URL=getenv("COOKIES_URL" , "https://gist.githubusercontent.com/sparrow9616/f29fc6588086a3c72d92dd9c03773350/raw/4229f3f4aab4a6693fc0794d136d30f54d67ae85/gistfile1.txt")

## Other vaes
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 300))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID","-1002136457746"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6391774843))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","moonss")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-417b5d4b-0c2c-4442-a551-21a2faad12d6")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/mooncodessssss/ai",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MoonMusic_Updates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/MoonMusic_Updates")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
ASSISTANT_LEAVE_TIME = int(getenv("ASSISTANT_LEAVE_TIME",  5400))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 204857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes

PRIVATE_BOT_MODE_MEM = int(getenv("PRIVATE_BOT_MODE_MEM", 1))


CACHE_DURATION = int(getenv("CACHE_DURATION" , "86400"))  #60*60*24
CACHE_SLEEP = int(getenv("CACHE_SLEEP" , "3600"))   #60*60


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION","BQFmGd8AlEej0AS5VtryW7kEnd-HuJ8PKua0Unf0BhLvBSGLrj1hBuzdS46xaO1jHd14IWYZM3dr0Ir5ZHsWmZcjBAyYXF3YDH0GPBmVzuwVIo2oAgBnwdB0CBgekonbjZ8VhOUQkWmKf3XdEZk0hkGXzey0HDhwLCnl14NnvQMGwWV5g4QMvhcXmfGrCv45eCCmGsVCweOgxdi9cu23tTCCC4TDgc4iCVfHp9hBmgdziVo7riPWppeHWaed3EnXgeWwSRNQlj1K1ffTL1YMvAJMpe0wyibcGCRTXrIPvjjb-IolS1oGrbU2vfWG7BvgS8lialLXLcrR6cHMpQQC8B5fX1xSDgAAAAGqavXKAA")
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
file_cache: dict[str, float] = {}

START_IMG_URL = getenv(
    "START_IMG_URL", "https://i.ibb.co/k3cw8XS/IMG-20250103-174108-968.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://i.ibb.co/h9XdzGp/IMG-20250103-174105-243.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://i.ibb.co/h9XdzGp/IMG-20250103-174105-243.jpg"
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


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:360"))


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
