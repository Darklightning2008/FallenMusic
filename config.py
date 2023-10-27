from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/401717b6f0ba3b81c9b47.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/d50559616352ad2e27b05.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LovelyXSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LovelyXAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/7e98c502bc975cc5d045c.jpg"
