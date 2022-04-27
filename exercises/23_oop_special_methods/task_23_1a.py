# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""

from pprint import pprint
import ipaddress
import re

class IPAddress:
    def __init__(self,network):
        self.network = network
        ip = self.network.split('/')[0]
        mask = int(self.network.split('/')[1])
        match_ip = re.search(r'\d+\.\d+\.\d+\.\d+', ip)
        if match_ip and ipaddress.IPv4Address(ip):
            pass
        else:
            raise ValueError(f"Incorrect IPv4 address")
        if not mask in range(8,33):
            raise ValueError(f"Incorrect mask")
        self.ip = ip
        self.mask = mask
    def __str__(self):
        return f"IP address {self.network}"
    def __repr__(self):
        return f"IPAddress('{self.network}')"


if __name__ == "__main__":
    ip1 = IPAddress('10.1.1.1/24')
    ip_list = []
    ip_list.append(ip1)
    print(ip_list)