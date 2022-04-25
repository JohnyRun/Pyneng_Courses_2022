# -*- coding: utf-8 -*-

"""
Задание 22.1d

Изменить класс Topology из задания 22.1c

Добавить метод add_link, который добавляет указанное соединение, если его еще
 нет в топологии.
Если соединение существует, вывести сообщение "Такое соединение существует",
Если одна из сторон есть в топологии, вывести сообщение
"Cоединение с одним из портов существует"


Создание топологии
In [7]: t = Topology(topology_example)

In [8]: t.topology
Out[8]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [9]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))

In [10]: t.topology
Out[10]:
{('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
 ('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
 ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
 ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
 ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
 ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
 ('R3', 'Eth0/2'): ('R5', 'Eth0/0')}

In [11]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/0'))
Такое соединение существует

In [12]: t.add_link(('R1', 'Eth0/4'), ('R7', 'Eth0/5'))
Cоединение с одним из портов существует


"""
from pprint import pprint

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}

class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)
    def _normalize(self,topology_dict):
        new_dict = topology_dict.copy()
        for key, value in topology_dict.items():
            if topology_dict.get(value) == key and new_dict.get(value) == key:
                del new_dict[key]
        return new_dict
    def delete_link(self,link1,link2):
        if self.topology.get(link1) == link2:
            del self.topology[link1]
        elif self.topology.get(link2) == link1:
            del self.topology[link2]
        else:
            print('Такого соединения нет')
    def delete_node(self,device):
        temp_topology = self.topology.copy()
        flag = False
        for item in temp_topology.items():
            if device == item[0][0] or device == item[1][0]:
                del self.topology[item[0]]
                flag = True
        if not flag:
            print('Такого соединения нет')
    def add_link(self,link1,link2):
        if self.topology.get(link1) == link2:
            print('Такое соединение существует')
        elif link1 in self.topology.keys() or link2 in self.topology.keys():
            print('Cоединение с одним из портов существует')
        elif link1 in self.topology.values() or link2 in self.topology.values():
            print('Cоединение с одним из портов существует')
        else:
            self.topology[link1] = link2


if __name__ == "__main__":
    top = Topology(topology_example)
    pprint(top.topology)
    print('#######################')
    top.add_link(('R2', 'Eth0/4'), ('R7', 'Eth0/0'))
    pprint(top.topology)