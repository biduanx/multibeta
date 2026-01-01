import os

from dotenv import load_dotenv

load_dotenv(".env")

DEVS = [7366711345, 8342493610]

KYNAN = list(map(int, os.getenv("KYNAN", "7366711345").split()))

API_ID = int(os.getenv("API_ID", ""))

API_HASH = os.getenv("API_HASH", "")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

SESSION = os.getenv("SESSION", "")

OWNER_ID = int(os.getenv("OWNER_ID", "7366711345"))

USER_ID = list(map(int, os.getenv("USER_ID", "7366711345 8342493610 8074843893").split()))

LOG_UBOT = int(os.getenv("LOG_UBOT", ""))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001876092598 -1001864253073 -1001451642443 -1001825363971 -1001797285258 -1001927904459 -1001287188817 -1001812143750 -1001608701614 -1001473548283 -1001675459127 -1001938303588 -1001861414061").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "10"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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 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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "",
)
