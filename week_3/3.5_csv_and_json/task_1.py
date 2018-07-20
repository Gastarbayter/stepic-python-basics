"""
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

Файл с данными:
Crimes.csv
"""

import csv

from dateutil import parser

primes_type = []
with open("for_task_1/Crimes.csv") as f:
    crime_reader = csv.DictReader(f)

    crimes_2015 = {}

    for line in crime_reader:
        if parser.parse(line["Date"]).year == 2015:
            if line["Primary Type"] in crimes_2015:
                crimes_2015[line["Primary Type"]] += 1
            else:
                crimes_2015[line["Primary Type"]] = 1

print(max(crimes_2015, key=crimes_2015.get))
