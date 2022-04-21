# -*- coding: utf-8 -*-
"""
Задание 21.3

Создать функцию parse_command_dynamic.

Параметры функции:
* command_output - вывод команды (строка)
* attributes_dict - словарь атрибутов, в котором находятся такие пары ключ-значение:
 * 'Command': команда
 * 'Vendor': вендор
* index_file - имя файла, где хранится соответствие между командами и шаблонами.
  Значение по умолчанию - "index"
* templ_path - каталог, где хранятся шаблоны. Значение по умолчанию - "templates"

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br.
"""
from pprint import pprint
from textfsm import clitable
import textfsm

attributes = {'Command':'sh ip int br', 'Vendor':'cisco_ios'}

def parse_command_dynamic(command_output, attributes_dict, templ_path='templates', index_file='index'):
    result_list = []
    with open(command_output,'r') as f:
        output_sh_ip_int_br = f.read()
    cli_table = clitable.CliTable(index_file, templ_path)
    cli_table.ParseCmd(output_sh_ip_int_br,attributes_dict)
    data_rows = [list(row) for row in cli_table]
    for row in data_rows:
        result_list.append(dict(zip(cli_table.header, row)))
    return result_list


if __name__ == "__main__":
    pprint(parse_command_dynamic('output/sh_ip_int_br.txt', attributes))