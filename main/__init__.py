#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("29300367", default=None, cast=int)
API_HASH = config("ee64d4b0b46a227b961d7d4c16c1116e", default=None)
BOT_TOKEN = config("6824047904:AAHz14ANer9BcNFoVJAeY-cv2LgefhS2aUk", default=None)
SESSION = config("BQG_Fo8ACJiDo_M_MGTWXwblEMfPNkdBKnsSLmCcm4ZGxMvlnUe1bHpp2Pr8XNoHXT0VKUX2off5amYCIwJj3plY8KZ7c9H9OTaq_VJRFavUdfjfly4x-dzd37srf3Omzvv3l0xqpKv3vdHT2MpkxvarvyijR7Z_j9DQPXZ64gfynt9SNoEgzojp8KtcwVHR716TkHrfiOzwRq3Dny7BYmvIDfr-kZXd6IMe6bsG21xNFn4BJJKXbhdkKZ51NgRPbgqwC0bNVsNiNY_V2pmj1Vp2R68PfKBw7U5D--ydB3qRMSNmwBYUi8krqPziW5NvAS4Daavzr9gj8O2NN6acFC0b-MEO2gAAAAGWvrUgAQ", default=None)
FORCESUB = config("ave5656", default=None)
AUTH = config("680627177", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
