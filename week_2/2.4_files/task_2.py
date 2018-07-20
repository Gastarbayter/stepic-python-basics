"""
Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом порядке.
"""
import os.path
import zipfile

with zipfile.ZipFile('for_task_2/main.zip', 'r') as archive, open('for_task_2/output.txt', 'w') as output:
    nms = sorted(set([os.path.dirname(nm) for nm in archive.namelist() if ".py" in nm]))
    print(*nms, sep="\n", file=output)
