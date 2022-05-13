import sqlite3
from sys import argv

parameter = argv[0]
value = argv[1]
correct_parameters = ['mac', 'ip', 'vlan', 'interface', 'switch']

def request_to_table(param=None,value=None):
    if param and value:
        if param in correct_parameters:
            try:
                connection = sqlite3.connect('dhcp_snooping.db')
                cursor = connection.cursor()
                cursor.execute(f'select * from dhcp where {param} = "{value}"')
            except sqlite3.IntegrityError as e:
                print(f'При выполнении запроса с параметрами: {param} и {value} возникла ошибка {e}')
        else:
            print('Данный параметр не поддерживается.')
            print('Допустимые значения параметров: mac, ip, vlan, interface, switch')