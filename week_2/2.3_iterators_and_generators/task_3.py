"""
Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода simplecrypt.encrypt.

Вам необходимо установить библиотеку simple-crypt, и с помощью метода simplecrypt.decrypt узнать, какой из паролей служит ключом для расшифровки файла с интересной информацией.

Ответом для данной задачи служит расшифрованная интересная информация Алисы.

Файл с информацией
Файл с паролями

Примечание:
Для того, чтобы считать все данные из бинарного файла, можно использовать, например, следующий код:

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
"""

import multiprocessing

import simplecrypt


def decrypt(data, password):
    try:
        res = simplecrypt.decrypt(password, data)
        print(res)
    except simplecrypt.DecryptionException:
        print("Password: {} is wrong".format(password))


with open("for_task_3/encrypted.bin", "rb") as ef, open("for_task_3/passwords.txt", "r") as pwd:
    data = ef.read()
    processes = []

    for p in pwd:
        password = p.rstrip()
        t = multiprocessing.Process(target=decrypt, args=(data, password))
        processes.append(t)
        t.start()

    for t in processes:
        t.join()
