# -*- coding: utf-8 -*-
"""
Задание 21.1a

Создать функцию parse_output_to_dict.

Параметры функции:
* template - имя файла, в котором находится шаблон TextFSM.
  Например, templates/sh_ip_int_br.template
* command_output - вывод соответствующей команды show (строка)

Функция должна возвращать список словарей:
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на выводе команды output/sh_ip_int_br.txt
и шаблоне templates/sh_ip_int_br.template.
"""

from pprint import pprint
import textfsm

def parse_output_to_dict(template, command_output):
    with open(template) as f, open(command_output) as output:
        re_table = textfsm.TextFSM(f)
        return re_table.ParseTextToDicts(output.read())

# вызов функции должен выглядеть так
if __name__ == "__main__":
    result = parse_output_to_dict("templates/sh_ip_int_br.template", 'output/sh_ip_int_br.txt')
    pprint(result)