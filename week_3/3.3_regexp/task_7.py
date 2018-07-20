"""
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
"""

import re
import sys

for line in (line.rstrip() for line in sys.stdin):
    print(re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE))
