#! /usr/bin/env python3

import sqlite3
from sys import argv
from pprint import pprint

correct_parameters = ['mac', 'ip', 'vlan', 'interface', 'switch']

def request_to_table(param=None,value=None):
    connection = sqlite3.connect('dhcp_snooping.db')
    cursor = connection.cursor()
    if param and value:
        if param in correct_parameters:
            try:
                 print('Активные записи:')
                 cursor.execute(f'select * from dhcp where {param} = "{value}" and active="1"')
                 pprint(cursor.fetchall())
                 print('Нективные записи:')
                 cursor.execute(f'select * from dhcp where {param} = "{value}" and active="0"')
                 pprint(cursor.fetchall())
            except sqlite3.IntegrityError as e:
                  print(f'При выполнении запроса с параметрами: {param} и {value} возникла ошибка {e}')
        else:
            print('Данный параметр не поддерживается.')
            print(f'Допустимые значения параметров: {correct_parameters}')
    else:
        print('Активные записи:')
        cursor.execute('select * from dhcp where active="1"')
        pprint(cursor.fetchall())
        print('Нективные записи:')
        cursor.execute('select * from dhcp where active="0"')
        pprint(cursor.fetchall())


if __name__ == '__main__':
    if len(argv) == 3:
        param = argv[1]
        value = argv[2]
        request_to_table(param,value)
    elif len(argv) == 1:
        request_to_table()
    elif len(argv) == 2 or len(argv) > 3:
        print('Скрипт поддерживает 0 или 2 аргумента')