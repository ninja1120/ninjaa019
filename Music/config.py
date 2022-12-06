##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('BABPcMjF2K84lO81b7YToJG2GLvLc61LFFlsGdTSwl9TjWrkY_IpB6CNfNXjxjiY4joNbQBjAJdzGC7ZIpIQhntPUtMn_bXHQWwk4o0ZfEJQFYaQ2BxrPz764uh_1FWFTvLp8eivzS4s9DSaLDAz7uh8Wh33nEvY61PGiB-KCCMNWtVKXLeHBDO_RAYQwYLi-q-cDbf-SfuYdzDtgrwZn5UdTeyF8uqgmTOQIR8fXVG8QFzOptltK2RTLFyghr6g7lMYHeLwNocga-jC1_TDyugANa-7efDyHlucOy74ES__mSDF71N48bBV0NGh-K1egKHiobPz6FFt0y8LIGQIX1Q3AAAAAVNJtXsA', 'session')
BOT_TOKEN = getenv('5698925550:AAH49bVAzDsCMQ9JK49EHJklcoY7Qo_1vtE')
API_ID = int(getenv('API_ID', "6464040"))
API_HASH = getenv('d6a6142d2ffa55f048adb8f999b9415d')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '3600'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("mongodb+srv://ahmedninjaa011:ahmed@112003@cluster0.cvcb1rq.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '5659728707').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001513000619)
ASS_ID = int(getenv("ASS_ID", '5692306811'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '5659728707').split()))
GROUP = getenv("GROUP", None)
CHANNEL = getenv("CHANNEL", None)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ninja1120/KyyMusic")
AUTO_LEAVE = int(getenv("AUTO_LEAVE", "1500"))
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# KALO FORK/CLONE JAN DI HAPUS KENTOD
OWNER_ID.append(1663258664)
OWNER_ID.append(1607338903)
