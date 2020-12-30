import time
import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
VK_TOKEN = os.getenv('VK_TOKEN')
SID = os.getenv('SID')
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')
client = Client(SID, TOKEN)


def get_status(user_id):
    params = {
        'user_ids': user_id,
        'v': '5.92',
        'access_token': VK_TOKEN,
        'fields': 'online'
    }
    info_user = requests.post(
        'https://api.vk.com/method/users.get',
        params=params
        )
    is_online = info_user.json().get('response')[0].get('online')
    return is_online


def send_sms(sms_text):
    message = client.messages.create(
        to=NUMBER_TO,
        from_=NUMBER_FROM,
        body=sms_text
    )
    return message.sid


if __name__ == '__main__':
    vk_id = input('Введите id ')
    while True:
        if get_status(vk_id) == 1:
            send_sms(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
