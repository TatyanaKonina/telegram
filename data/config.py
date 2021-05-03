import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins = [
    1184689415
]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

