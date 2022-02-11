# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

vlan = input('Введите номер VLAN: ')

result_list = []
#vlan = int(vlan)

with open('CAM_table.txt') as file:
    for line in file:
        line = line.split()
        if line:
            if line[0].isdigit():
                result_list.append(line)
for value in result_list:
    value[0] = int(value[0])
    value.remove('DYNAMIC')

result_list = sorted(result_list)

for i in result_list:
    if int(vlan) == i[0]:
        print('{:5} {:>20} {:>10}'.format(i[0],i[1], i[2]))
    else:
        continue