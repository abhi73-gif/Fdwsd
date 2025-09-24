# DON'T add anything here just add in render's secret or env section 
from os import environ

API_ID = int(environ.get("20937420", ""))
API_HASH = environ.get("09d7f6744feb17759304df65666961da", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

