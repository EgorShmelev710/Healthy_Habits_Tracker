import requests
from django.conf import settings
from django.utils.timezone import localtime

from rest_framework import status


def send_telegram(habit):
    local_habit_time = localtime(habit.time)
    formatted_time = local_habit_time.strftime('%H:%M')

    text = f'Привет! Пора {habit.action}! У вас это было запланировано на сегодня на {formatted_time}'
    chat_id = habit.user.tg_chat_id
    params = {
        'text': text,
        'chat_id': chat_id
    }

    response = requests.post(f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage', data=params)
    if response.status_code != status.HTTP_200_OK:
        print(f"Ошибка при отправке сообщения в Telegram: {response.text}")
