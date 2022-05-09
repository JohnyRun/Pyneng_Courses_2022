import re
import sqlite3
import yaml
from pprint import pprint
import os
from create_db import create_database

def add_switch_information(switch_config_yaml, connection_name):
    '''
    :param configname: file.yaml
    '''
    print('Добавляю данные в таблицу switches')
    with open(switch_config_yaml) as f:
        switches_information = yaml.safe_load(f)
        for switches in switches_information.values():
            for key,value in switches.items():
                tup = tuple([key,value])
                try:
                    query = '''insert into switches (hostname, location)
                                       values (?, ?)'''
                    connection_name.execute(query, tup)
                    connection_name.commit()
                except sqlite3.IntegrityError as e:
                    print(f'При добавлении данных {tup} Возникла ошибка: {e}')

def dhcp_snooping_information(dhcp_snooping_output, connection_name):
    print('Добавляю данные в таблицу dhcp')
    result = []
    switch_name = dhcp_snooping_output.split('_')[0]
    regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    with open(dhcp_snooping_output) as file:
        for line in file.readlines():
            match = regex.search(line)
            if match:
                temp_list = list(match.groups())
                temp_list.append(switch_name)
                result.append(tuple(temp_list))
    for row in result:
        try:
            query = '''insert into dhcp (mac, ip, vlan, interface, switch)
                               values (?, ?, ?, ?, ?)'''
            connection_name.execute(query, row)
            connection_name.commit()
        except sqlite3.IntegrityError as e:
            print(f'При добавлении данных {row} Возникла ошибка: {e}')



if __name__ == '__main__':
    db_filename = 'dhcp_snooping.db'
    db_exists = os.path.exists(db_filename)
    filenames = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    if db_exists:
        connection = sqlite3.connect(db_filename)
        cursor = connection.cursor()
        #add_switch_information('switches.yml',connection)
        #for filename in filenames:
        #    dhcp_snooping_information(filename, connection)
        cursor.execute('select * from switches')
        pprint(cursor.fetchmany(10))
        cursor.execute('select * from dhcp')
        pprint(cursor.fetchmany(10))
    else:
        print('База данных не существует. Перед добавлением данных, ее надо создать')
        create_database('dhcp_snooping.db')