# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""

from tabulate import tabulate

ip_list1 = ['10.1.1.1','10.1.1.2','5.5.5.5','99.6.2.1']
ip_list2 = ['10.1.1.7', '10.1.1.8', '10.1.1.9','192.168.5.4']

def print_ip_table(reachable_ip_list, unreacheble_ip_list):
    columns = ['Reachable','Unreachable']
    result_list = []
    counter = 0
    for ip in reachable_ip_list:
        result_list.append([ip])
    if len(reachable_ip_list) < len(unreacheble_ip_list):
        for i in range(len(unreacheble_ip_list) - len(reachable_ip_list)):
            result_list.append([''])
    for ip in unreacheble_ip_list:
        if counter > len(unreacheble_ip_list):
            break
        result_list[counter].append(ip)
        counter += 1
    print(tabulate(result_list, headers=columns))

if __name__ == '__main__':
    print_ip_table(ip_list1, ip_list2)
