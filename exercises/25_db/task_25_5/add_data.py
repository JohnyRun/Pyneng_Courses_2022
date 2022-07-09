import re
import sqlite3
import yaml
from pprint import pprint
import os
import sys
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
    cursor = connection_name.cursor()
    result = []
    mac_list_from_file = []
    switch_name = dhcp_snooping_output.split('_')[0]
    regex = re.compile(r'(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')
    with open(dhcp_snooping_output) as file:
        for line in file.readlines():
            match = regex.search(line)
            if match:
                temp_list = list(match.groups())
                temp_list.append(switch_name)
                result.append(tuple(temp_list))
    for mac in result:
        mac_list_from_file.append(mac[0])
    for row in result:
        try:
            query = '''replace into dhcp (mac, ip, vlan, interface, switch, active,last_active)
                               values (?, ?, ?, ?, ?, 1, datetime('now'))'''
            connection_name.execute(query, row)
            connection_name.commit()
        except sqlite3.IntegrityError as e:
            print(f'При добавлении данных {row} Возникла ошибка: {e}')
    for line in cursor.execute('select mac from dhcp'):
        if line[0] not in mac_list_from_file:
            connection_name.execute(f'update dhcp set active = "0" where mac="{line[0]}"')
            connection_name.commit()


if __name__ == '__main__':
    db_filename = 'testBase.db'
    filenames = ['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt']
    new_filenames = ['new_data/sw1_dhcp_snooping.txt', 'new_data/sw2_dhcp_snooping.txt', 'new_data/sw3_dhcp_snooping.txt']
    #create_database('testBase.db')
    connection = sqlite3.connect(db_filename)
    cursor = connection.cursor()
    #for file in filenames:
        #dhcp_snooping_information(file,connection)
    dhcp_snooping_information(filenames[0], connection)
    cursor.execute('select * from dhcp')
    pprint(cursor.fetchmany(13))
