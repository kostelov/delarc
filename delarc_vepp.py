# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import datetime
from re import match


def hlp():
    print('''
    Утилита работает с типом архива .tgz и файлами с начальным именем backup_
    !!! ВАЖНО: Утилита не удалит файл, если он в единсвенном экземпляре !!!
    help - вызов этой справки
    del <n> - удаление архива старше n дней
    test <n> - запуск утилиты в тестовом режиме без удаления файлов
    ''')


def test():
    backupdir = '/media/7dc696fd-4e30-45a5-b4d4-38342d5102ed/backup/'
    pattern = r'(^[0-9]+)'
    fdel = []
    for name in os.listdir(backupdir):
        fullname = os.path.join(backupdir, name)
        if os.path.isfile(fullname):
            if name.startswith('backup_') and name.endswith('.tgz'):
                fdate = datetime.datetime.fromtimestamp(os.path.getmtime(fullname)).date()
                curdate = datetime.datetime.today().date()
                if int(match(pattern, str(curdate - fdate)).group()) >= int(days):
                    fdel.append(fullname)
    with open('/media/7dc696fd-4e30-45a5-b4d4-38342d5102ed/backup/delarc.log', 'a', encoding='utf-8') as file:
        file.write('\n -test- {} -test- \n'.format(datetime.datetime.today().date()))
        fdel.sort()
        for name in fdel:
            file.write('{} - будет удален \n'.format(name))


def deltgz():
    backupdir = '/media/7dc696fd-4e30-45a5-b4d4-38342d5102ed/backup/'
    pattern = r'(^[0-9]+)'
    count = 0
    fdel = []
    for name in os.listdir(backupdir):
        fullname = os.path.join(backupdir, name)
        if os.path.isfile(fullname):
            if name.startswith('backup_') and name.endswith('.tgz'):
                fdate = datetime.datetime.fromtimestamp(os.path.getmtime(fullname)).date()
                curdate = datetime.datetime.today().date()
                if int(match(pattern, str(curdate - fdate)).group()) >= int(days):
                    fdel.append(fullname)
                    count += 1
    with open('/media/7dc696fd-4e30-45a5-b4d4-38342d5102ed/backup/delarc.log', 'a', encoding='utf-8') as file:
        file.write('\n  --- {} --- \n'.format(datetime.datetime.today().date()))
        fdel.sort()
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
