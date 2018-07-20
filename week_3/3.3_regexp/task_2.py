"""
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.

Примечание:
Для работы со словами используйте группы символов \b и \B.
Описание этих групп вы можете найти в документации.
"""

import re
import sys

for line in (line.rstrip() for line in sys.stdin):
    if re.search(r'\bcat\b', line):
        print(line)
