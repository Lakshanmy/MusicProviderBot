from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQB3q8Mp8oseI4wrG8NPZWJJ8crl3UaGOztHnQDr2Z14fjmqY7hQnJFMilhhaz8ICq4bvlPO_g8Epdfi-B4gG1vHxa5DnH4K3SFlLg66QtAsQnOBPuQla3EM5_PHV29fvbzFk40xJfxLDGk9a9e8-nGMXON5kUO6RmRWV00T_FikPRDrQsLslXtTT24fbxD7z6VMfUAt4FEbH96qrN90EpEBR4WmVCzLfOFrBYgaW2v-Cpm1iopV3hChJUAM1Jt_P8gwCjk4FTDsZsGekzZN2Dl7YiD5lVQ84_L6sX8xC1G_lUFMk5__btwKUIta0hNzB6poYde8X2y4-JTN8QZpT48LSWga1gA")
BOT_TOKEN = getenv("BOT_TOKEN", "1929574866:AAGeg3HUMi5DV0EryU2TyQsIxDsq5n5PuJo")
BOT_NAME = getenv("BOT_NAME", "MusicPlayer Bot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "unlimitedworld_TM_channel")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "2987477"))
API_HASH = getenv("API_HASH", "fab0ac420d45ae0aea6be644017b5c4e")
BOT_USERNAME = getenv("BOT_USERNAME", "musicPlayer_FF_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MusicPlayer_zone")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "unlimitedworld_TM_group")
PROJECT_NAME = getenv("PROJECT_NAME", "🎧 Music Player Bot 🎧")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ASHIRUMALSHAN/MusicProviderBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "3000"))
ARQ_API_KEY = getenv("ARQ_API_KEY", "VLCFLT-EQMWZO-LSKBRT-OVMJDL-ARQ")
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
