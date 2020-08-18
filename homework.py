import os
import requests
import telegram
import time
from dotenv import load_dotenv

load_dotenv()


PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')


        
        
def send_message(message): 
    bot = telegram.Bot(token=TELEGRAM_TOKEN) 
    return bot.send_message(chat_id=CHAT_ID, text=message) 
 
send_message('привет')
