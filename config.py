from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/e2a9e9b93b49a5d6ae0ef.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/e2a9e9b93b49a5d6ae0ef.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LovelyXSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/LovelyXAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/e2a9e9b93b49a5d6ae0ef.jpg"
