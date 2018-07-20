"""
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
"""

import re
import sys

for line in (line.rstrip() for line in sys.stdin):
    if re.search(r'\\', line):
        print(line)
