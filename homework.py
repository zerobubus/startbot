import os 
import requests 
import telegram 
import time 
import requests
from dotenv import load_dotenv 
 
load_dotenv() 
 
 
PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN') 
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN') 
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID') 
TOKEN = os.getenv('TOKEN')
VERSION = os.getenv('VERSION')
VK_ID = os.getenv('VK_ID')
 
        
     
def get_status(user_id):

    params = {'v': version,
           'access_token': token,
           'user_ids': user_id,
           'fields': 'online'
    }
    status = requests.post(f'https://api.vk.com/method/users.get', params=params)
    return status.json()['response'][0]['online']

                
def send_message(message):  
    bot = telegram.Bot(token=TELEGRAM_TOKEN)  
    return bot.send_message(chat_id=CHAT_ID, text=message)  
  
 

if __name__ == "__main__":
    
    while True:
        if get_status(VK_ID) == 1:
            send_message(f'{VK_ID} сейчас онлайн!')
            break
        time.sleep(5)
