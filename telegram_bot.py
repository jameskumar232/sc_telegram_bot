import requests
import time
from telegram import Bot
from telegram.error import TelegramError

# Your Telegram Bot API key
API_KEY = '7340152765:AAF9zS3kHSYEfCfrh1EgsQNFInEdidNkQFY'
bot = Bot(token=API_KEY)

# Telegram chat_id where the image will be sent (update with your chat ID)
CHAT_ID = 'YOUR_CHAT_ID'

# URL to check for the online status
JSON_URL = 'https://mybro.tv/api/v1/models/alias/novapol'

def check_status_and_update():
    while True:
        try:
            response = requests.get(JSON_URL)
            data = response.json()

            if data.get('isOnline'):
                image_url = data.get('thumbnailImageLivePopular')
                bot.send_photo(chat_id=CHAT_ID, photo=image_url)
                time.sleep(60)
            else:
                print("Model is offline.")
                time.sleep(300)
        except TelegramError as e:
            print(f"Telegram error: {e}")
            time.sleep(60)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

if __name__ == '__main__':
    check_status_and_update()
