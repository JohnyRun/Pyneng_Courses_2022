# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

switchport_all_modes = []
switchport_all_modes.append(access_template[0].split()[2])
switchport_all_modes.append(trunk_template[1].split()[2])
dict_switch_mode = {'access':access_template, 'trunk':trunk_template}

banner_dict = {'access':'Введите номер VLAN:','trunk':'Введите разрешенные VLANы:'}

switchport_mode = input(f"Введите режим работы интерфейса {switchport_all_modes}: ")
interface = input('Введите тип и номер интерфейса в формтате Fa0/1:  ')
vlans = input(banner_dict[switchport_mode])

print(f"interface {interface}")
print('\n'.join(dict_switch_mode[switchport_mode]).format(vlans))