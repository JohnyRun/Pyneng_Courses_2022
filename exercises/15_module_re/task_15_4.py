# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример итогового списка:
["Loopback0", "Tunnel0", "Ethernet0/1", "Ethernet0/3.100", "Ethernet1/0"]

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""
import re
from pprint import pprint

def get_ints_without_description(filename):
    result_list = []
    ports_with_description = []
    interfaces_types = ['Loopback']
    with open(filename) as file:
        file = file.read()
        for line in file.split('\n'):
            if line.startswith('interface'):
                result_list.append(line.split()[-1])
        port_iter = re.finditer(r'interface \S+'
                          r'\s+description',file)
        for match in port_iter:
            ports_with_description.append(match.group().split('\n')[0])
        ports_with_description = [x.split()[-1] for x in ports_with_description]
        for port in ports_with_description:
            result_list.remove(port)
        return result_list


if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))