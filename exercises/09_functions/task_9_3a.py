# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map(config_filename):
    with open(config_filename) as file:
        access_dict = {}
        trunk_dict = {}
        check_vlan_1 = False
        for line in file:
            if 'interface Fast' in line:
                check_vlan_1 = False
                port = line.split()[-1]
            elif 'access vlan' in line:
                access_dict[port] = int(line.split()[-1])
            elif 'trunk allowed vlan' in line:
                vlan_list = line.split()[-1].split(',')
                vlan_list = [int(vlan) for vlan in vlan_list]
                trunk_dict[port] = vlan_list
            else:
                if 'mode access' in line:
                    access_dict[port] = 1
    result_list = [access_dict, trunk_dict]
    return tuple(result_list)

if __name__ == '__main__':
    print(get_int_vlan_map('config_sw2.txt'))