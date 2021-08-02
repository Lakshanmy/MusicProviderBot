from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQCLyYrmsi1pwhOBJpEj9Sv-fowYNtjp_rOtt5fe8Lz-e9ewiLH6vwZWQfEoPp_JkXzffJMdMqj15AeWi5W4HoPZtI0Swh7awOwqe6UZFGj7S1FMenKt1fwHzyUcB0IurYa0MOiad-LX0vymEOcPo3PzVaIWUfAzFib_wmlmzWvMkKzoJBTAA-Xbwiexghs2oRBgbFls8OqyBTIGIq16QK8DbiVL6yQgM0NSTCalrBLzqUKm74wMtF9KDJI9aq6gr0GxY9k_jBTNK86lg1S2524AsAD_hUlhanVinYQ45U9cI5saJ1dfJXaSDH9TKkwJ8jBC395sD6yV7iwN5zoCAhJ9VOFnuAA")
BOT_TOKEN = getenv("BOT_TOKEN", "1881233435:AAFdghFULQV5Hq1cYh-Nf9vYUuDsEkfZadA")
BOT_NAME = getenv("BOT_NAME", "uwmusicproviderbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "unlimitedworld_TM_channel")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "3866700"))
API_HASH = getenv("API_HASH", "629f9f3c93bf94c9276722876ca610a1")
BOT_USERNAME = getenv("BOT_USERNAME", "UwMusicProviderBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "UwMusicProvider")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "unlimitedworld_TM_group")
PROJECT_NAME = getenv("PROJECT_NAME", "🎧 Music Provider Bot 🎧")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ASHIRUMALSHAN/MusicProviderBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "2000"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "VLCFLT-EQMWZO-LSKBRT-OVMJDL-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
