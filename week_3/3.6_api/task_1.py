"""
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""

import requests

number_url = "http://numbersapi.com/{}/math"

parameters = {"default": "Boring", "json": True}

out = open("for_task_1/output.txt", "w")

with open("for_task_1/input.txt") as dataset:
    for num in dataset:
        resp = requests.get(number_url.format(int(num)), params=parameters)
        json_data = resp.json()

        if json_data["text"] == parameters["default"]:
            print(json_data["text"], file=out)
        else:
            print("Interesting", file=out)

out.close()
