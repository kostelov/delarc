# -*- coding: utf-8 -*-
import os
import sys
import datetime
from re import match


def hlp():
    print('''
    Утилити работает с типом архива .tgz и файлами с начальным именем backup_
    !!! ВАЖНО: Утилита не удалит файл, если он в единсвенном экземпляре !!!
    help - вызов этой справки
    del <n> - удаление архива старше n дней
    test <n> - запуск утилиты в тестовом режиме без удаления файлов
    ''')


def test():
    pattern = r'(^[0-9]+)'
    fdel = []
    for name in os.listdir(os.getcwd()):
        fullname = os.path.join(os.getcwd(), name)
        if os.path.isfile(fullname):
            if name.startswith('backup_') and name.endswith('.tgz'):
                fdate = datetime.datetime.fromtimestamp(os.path.getmtime(name)).date()
                curdate = datetime.datetime.today().date()
                if int(match(pattern, str(curdate - fdate)).group()) >= int(days):
                    fdel.append(name)
    with open('delarc.log', 'a', encoding='utf-8') as file:
        file.write('\n -test- {} -test- \n'.format(datetime.datetime.today().date()))
        for name in fdel:
            file.write('{} - будет удален \n'.format(name))


def deltgz():
    pattern = r'(^[0-9]+)'
    count = 0
    fdel = []
    for name in os.listdir(os.getcwd()):
        fullname = os.path.join(os.getcwd(), name)
        if os.path.isfile(fullname):
            if name.startswith('backup_') and name.endswith('.tgz'):
                fdate = datetime.datetime.fromtimestamp(os.path.getmtime(name)).date()
                curdate = datetime.datetime.today().date()
                if int(match(pattern, str(curdate - fdate)).group()) >= int(days):
                    fdel.append(name)
                    count += 1
    with open('delarc.log', 'a', encoding='utf-8') as file:
        file.write('\n  --- {} --- \n'.format(datetime.datetime.today().date()))
        for name in fdel:
            if count > 1:
                os.remove(name)
                file.write('{} - удален \n'.format(name))
                count -= 1


do = {
    "help": hlp,
    "del": deltgz,
    "test": test
}
try:
    days = sys.argv[2]
except IndexError:
    days = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if do.get(key):
    do[key]()
else:
    print('Указан не верный параметр. help - для справки')
