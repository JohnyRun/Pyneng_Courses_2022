# -*- coding: utf-8 -*-

"""
Задание 23.3a

В этом задании надо сделать так, чтобы экземпляры класса Topology
были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
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
    def __add__(self, other):
        sum_topology = dict(self.topology)
        sum_topology.update(dict(other.topology))
        return Topology(sum_topology)
    def __getitem__(self, index):
        return tuple(dict(self.topology).items())[index]

if __name__ == '__main__':
    t1 = Topology(topology_example)
    for i in t1:
        pprint(i)