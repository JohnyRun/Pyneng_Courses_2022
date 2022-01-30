# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
network = input('Введите ip-адрес в формате:10.1.1.0/24:  ')
network = network.split('/')

template_network = """
        Network:
        {:<8}  {:<8}  {:<8}  {:<8}
        {:08b}  {:08b}  {:08b}  {:08b}
        """
template_mask = """
        Mask:
        /{}
        {:<8}  {:<8}  {:<8}  {:<8}
        {:<8}  {:<8}  {:<8}  {:<8}
        """

result_network_list = network[0]
mask = network[1]
mask_bin = '1' * int(mask) + '0' * (32-int(mask))
print(mask_bin[18:8])

print(template_network.format(int(result_network_list.split('.')[0]), int(result_network_list.split('.')[1]),
                              int(result_network_list.split('.')[2]), int(result_network_list.split('.')[3]),
                              int(result_network_list.split('.')[0]), int(result_network_list.split('.')[1]),
                              int(result_network_list.split('.')[2]), int(result_network_list.split('.')[3])))

print(template_mask.format(mask,int(mask_bin[0:8],2), int(mask_bin[8:16],2), int(mask_bin[16:24],2), int(mask_bin[24:32],2),
                           mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:32]))