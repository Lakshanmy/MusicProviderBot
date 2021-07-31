from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQBsro1uxWcAT88JhtgBu23t0uH3x7w7joeTyh7Qq2evQJ-GHrF3bkiQnIk8y-w280sc2GcCKaxbsZAVAhXDiK9whmSIXyFOLhxiLxNizN1dDelDgyyw5gs-A1kzz4ih67jVGpFlZ7PdcaibZ6LzDqvVMdEKpInLJ2S4T4-wGuDydxqlsyCRFBseNUxF_-VlvuXTLCR2PfC4ozVyPTdOAwlsv0H33hroioDqCW_QqgdMfeCUJQ9O3OoaZWeIpzjcCp58yie0eQZUJzXC3reRCTmrVEkPc1UQsuW3iWVEKq9CkwNP5HfTN97hBpLRPkDRavf0tiD7VXPlx0FKds9Wt1QqVOFnuAA")
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
LOG_GRP = getenv("LOG_GRP", "-1001505738728")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
