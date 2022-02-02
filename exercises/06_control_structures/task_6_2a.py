# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_address = input('Введите ip-адрес в формате 10.0.1.1: ')

ip_address_octets_list = ip_address.split('.')
new_ip_address_octets_list = []
true_flag = False

try:
    if len(ip_address_octets_list) != 4:
        true_flag = True
    elif ip_address.count('.') != 3:
        true_flag = True
    for ip in ip_address_octets_list:
        if int(ip) not in range(0,256):
            true_flag = True
            break
        else:
            new_ip_address_octets_list.append(int(ip))

    if not true_flag:
        if int(new_ip_address_octets_list[0]) in range(1,224):
            print('unicast')
        elif int(new_ip_address_octets_list[0]) in range(224,240):
            print('multicast')
        elif new_ip_address_octets_list[0] == '255' and new_ip_address_octets_list[1] == '255' and new_ip_address_octets_list[2] == '255' and new_ip_address_octets_list[3] == '255':
            print('local broadcast')
        elif new_ip_address_octets_list[0] == '0' and new_ip_address_octets_list[1] == '0' and new_ip_address_octets_list[2] == '0' and new_ip_address_octets_list[3] == '0':
            print('unassigned')
        else:
            print('unused')

except ValueError:
    true_flag = True

if true_flag:
    print('Неправильный IP-адрес')