import requests, os, asyncio,logging 
from pyrogram import Client, filters
from plugins import backgen

if os.path.exists("logs/Log.txt"):
    with open("logs/Log.txt", "r+") as f_d:
        f_d.truncate(0)

logging.basicConfig(level=logging.DEBUG,
           format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
           datefmt="%d-%b-%y %H:%M:%S",
           handlers=[RotatingFileHandler(
            "logs/Log.txt",
            maxBytes=1000000,
            backupCount=10),logging.StreamHandler()])

log = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)


bot_token = os.environ.get("BOT_TOKEN")
chatid = os.environ.get("FORWARD_ID")
api_id = os.environ.get("APIID")
api_hash = os.environ.get("APIHASH")

    

class Bot(Client):

    def __init__(self):
        super().__init__(
            session_name="BOT",
            api_id=api_id,
            api_hash=api_hash,
            bot_token=bot_token,
            plugins={"root": "plugins"},
        )

    async def start(self):
        await super().start()
        asyncio.get_event_loop().create_task(backgen())
        log.info("<<[Bot Started]>>")
    async def stop(self, *args):
        await super().stop()
        log.info("<<[Bot Stopped]>>")

app = Bot()
app.run()


