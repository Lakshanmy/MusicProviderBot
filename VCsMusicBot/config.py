from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQC9wkvFpv2jNsY5DMYeto6mqFL13Ad8cPTDG_U28CSYRBKbx3qBtpKTLoZQpdcdpTCu2BcXc73ipKc3wvyglWuc_NuUpMiF6Rc6plBPP5YLdJSEwDJ2SyYH88mSxa5mgTMJ58dLdydUBNbzo7CULHVFJDf3UStMJKpANxL_32J1to6C-phsZu6P-P9GRdmESn-UV1tc9i7dKgur5Po0ig9Wvzq1xVDg5jFHx-9N7QoQsHposaezjl67NlnFC-cBhXrJ-IO2sbjIL7gFI8WQhgLGMJ5N30iXpPpm1aNn_tQhiSKEPU6cZHv7QzTyHcqyEcAcu50UUaqIlxpiwlWLLzklVOFnuAA")
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
