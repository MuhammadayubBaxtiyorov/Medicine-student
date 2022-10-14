import requests

def send_telegram_message(msg, telegram_id):
    bot_token = "5632847942:AAFLAKfFj90TtS9l-gxvPpNIc7cSwT-T8l0"
    url  = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={telegram_id}&text={msg}"
    r = requests.get(url)
    return r.json()







