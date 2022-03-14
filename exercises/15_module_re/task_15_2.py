# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re

def parse_sh_ip_int_br(filename):
    result = []
    with open(filename) as file:
        for line in file:
            match_for_interfaces_up = re.search(r'(\S+)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+ +\w+ +(\w+)\s+(\w+)', line)
            match_for_interfaces_down = re.search(r'(\S+)\s+(\w{10})\s+\w+\s+\w+\s+(\w+\D+)\s+(\w+)', line)
            if match_for_interfaces_up:
                result.append(match_for_interfaces_up.groups())
            elif match_for_interfaces_down:
                result.append(match_for_interfaces_down.groups())
    return result

if __name__ == '__main__':
    print(parse_sh_ip_int_br('sh_ip_int_br.txt'))
