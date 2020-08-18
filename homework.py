import os
import requests
import telegram
import time
from dotenv import load_dotenv

load_dotenv()


PRACTICUM_TOKEN = os.getenv('PRACTICUM_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def parse_homework_status(homework):

    try: 
        homework_name = homework.get('homework_name')
        status = homework.get('status')
        if homework_name and status is not None:
            if status == 'rejected':
                verdict = 'К сожалению в работе нашлись ошибки.'
            else:
                verdict = 'Ревьюеру всё понравилось, можно приступать к следующему уроку.'
            return f'У вас проверили работу "{homework_name}"!\n\n{verdict}'
        else:
            return f'Данных нет, запрос вернулся пустым'  
    except Exception as e: 
        print(f'Бот упал с ошибкой: {e}')
           
    
def get_homework_statuses(current_timestamp):
    if current_timestamp is None:
        current_timestamp = int(time.time())
    headers = {'Authorization': f'OAuth {PRACTICUM_TOKEN}'}
    params ={'from_date': current_timestamp}
     
    try:
        homework_statuses = requests.get(
            'https://praktikum.yandex.ru/api/user_api/homework_statuses/', 
            headers=headers, params=params).json()
        return homework_statuses
    except Exception as e: 
        print(f'Бот упал с ошибкой: {e}') 
        
        
def send_message(message): 
    bot = telegram.Bot(token=TELEGRAM_TOKEN) 
    return bot.send_message(chat_id=CHAT_ID, text=message) 
 

def main(): 
    current_timestamp = int(time.time())  # начальное значение timestamp 
 
    while True: 
        try: 
            new_homework = get_homework_statuses(current_timestamp) 
            if new_homework.get('homeworks'): 
                send_message(parse_homework_status(new_homework.get('homeworks')[0])) 
            current_timestamp = new_homework.get('current_date')  # обновить timestamp 
            time.sleep(600)  # опрашивать раз в 10 минут 
 
        except Exception as e: 
            print(f'Бот упал с ошибкой: {e}') 
            time.sleep(10) 
            continue 
 
 
if __name__ == '__main__': 
    main() 
