from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "AQB3q8Mp8oseI4wrG8NPZWJJ8crl3UaGOztHnQDr2Z14fjmqY7hQnJFMilhhaz8ICq4bvlPO_g8Epdfi-B4gG1vHxa5DnH4K3SFlLg66QtAsQnOBPuQla3EM5_PHV29fvbzFk40xJfxLDGk9a9e8-nGMXON5kUO6RmRWV00T_FikPRDrQsLslXtTT24fbxD7z6VMfUAt4FEbH96qrN90EpEBR4WmVCzLfOFrBYgaW2v-Cpm1iopV3hChJUAM1Jt_P8gwCjk4FTDsZsGekzZN2Dl7YiD5lVQ84_L6sX8xC1G_lUFMk5__btwKUIta0hNzB6poYde8X2y4-JTN8QZpT48LSWga1gA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "UnlimiteWorldTeam")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cf19dda907391656338eb.png")
admins = {}
API_ID = int(getenv("API_ID", "2987477"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MusicPlayer_zone")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "SSH_Store")
PROJECT_NAME = getenv("PROJECT_NAME", "VC_MusicPlayer")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/ZauteKm/VCsMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "2000"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
