import json
import sys

import requests
import datetime


def getjson():
    payload = {
        'login': 'i.matyunin',
        'password': 'TrahOff2020'
    }
    with requests.Session() as s:
        s.post("https://lk.ulstu.ru/?q=auth/login", data=payload)

        r = s.get('https://time.ulstu.ru/api/1.0/timetable?filter=' + 'ИВТАПбд-31') # можно передавать сюда группу

        try:
            timetable = json.loads(r.text)
        except json.JSONDecodeError:
            print("Ошибка API! Проверьте логи и пароль.")
            sys.exit()

    return timetable


def get_current_week():
    september_1 = datetime.date(datetime.date.today().year, 9, 1)
    current_date = datetime.date.today()
    week_number = (current_date - september_1).days // 7 + 1
    current_week_day = datetime.date.today().weekday()

    return week_number, current_week_day


if __name__ == '__main__':
    timetable = getjson()
    current_week, current_day = get_current_week()
    # with open('ИВТАПбд-31.json', 'w') as f:
    for day in timetable["response"]["weeks"][f'{current_week}']["days"]:
        for lesson in timetable["response"]["weeks"][f'{current_week}']["days"][day["day"]]["lessons"]:
            print("группа " + lesson[0]["group"])
            print("предмет " + lesson[0]["nameOfLesson"])
            print("преподаватель " + lesson[0]["teacher"])
            print("аудитория " + lesson[0]["room"])
        print()
