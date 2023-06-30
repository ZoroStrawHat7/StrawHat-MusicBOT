from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/ece7789ffcadc96933fda.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/ece7789ffcadc96933fda.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/StrawHat_Support")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/StrawHat_Bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6260522360").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
