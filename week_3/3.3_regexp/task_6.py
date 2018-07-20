"""
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
"""

import re
import sys

for line in (line.rstrip() for line in sys.stdin):
    print(re.sub('human', 'computer', line))
