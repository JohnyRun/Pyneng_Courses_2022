# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re


def parse_sh_cdp_neighbors(filename):
    result_dict = {}
    include_dict1 = {}
    regex = (r'(?P<device>\S+)>[\S+ +]+'
             r'|(?P<device_id>\S+)\s+(?P<Local_int>\S+ \S+)\s+\d+\s+\S+\s+\S+\s+\S+\s+\S+\s+(?P<port_id>\S+ \S+)')
    match = re.findall(regex,filename)
    if match:
        for line in match:
           include_dict2 = {}
           if line[0]:
               hostname = line[0]
           else:
               include_dict2[line[1]] = line[3]
               include_dict1[line[2]] = include_dict2
               result_dict[hostname] = include_dict1
    return result_dict

if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt','r') as file:
        parse_sh_cdp_neighbors(file.read())