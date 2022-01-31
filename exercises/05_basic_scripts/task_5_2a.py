# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
network = input('Введите ip-адрес в формате:10.1.1.0/24:  ')
network = network.split('/')

template_network = """
        Network:
        {:<8}  {:<8}  {:<8}  {:<8}
        {:>08}  {:>08}  {:>08}  {:>08}
        """
template_mask = """
        Mask:
        /{}
        {:<8}  {:<8}  {:<8}  {:<8}
        {:<8}  {:<8}  {:<8}  {:<8}
        """

result_network_list = network[0]
mask = network[1]
bin_mask = '1' * int(mask) + '0' * (32-int(mask))
deligate_ip = result_network_list.split(".")
bin_ip = '{:08b}{:08b}{:08b}{:08b}'.format(int(deligate_ip[0]), int(deligate_ip[1]), int(deligate_ip[2]), int(deligate_ip[3]))
bin_ip_subnet = bin_ip[0:int(mask)] + '0'*(32-int(mask))

print(template_network.format(int(bin_ip_subnet[0:8],2), int(bin_ip_subnet[8:16], 2), int(bin_ip_subnet[16:24], 2), int(bin_ip_subnet[24:32], 2),
                              int(bin_ip_subnet[0:8]), int(bin_ip_subnet[8:16]), int(bin_ip_subnet[16:24]), int(bin_ip_subnet[24:32])))

print(template_mask.format(mask,int(bin_mask[0:8],2), int(bin_mask[8:16],2), int(bin_mask[16:24],2), int(bin_mask[24:32],2),
                           bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:32]))
