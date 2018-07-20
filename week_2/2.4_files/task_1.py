"""
Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

Пример входного файла:
ab
c
dde
ff

﻿Пример выходного файла:
ff
dde
c
ab
"""

with open('for_task_1/input.txt') as input_file, open('for_task_1/output.txt', 'w') as output_file:
    strings = [line.rstrip() for line in input_file]
    output_file.write('\n'.join(strings[::-1]))
