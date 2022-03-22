# -*- coding: utf-8 -*-
"""
Задание 17.2

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений
  и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv),
   в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена
  информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы (именно в этом порядке):
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается
на sh_vers. Вы можете раскомментировать строку print(sh_version_files),
чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.
"""

import glob
import csv
import re
from pprint import pprint

sh_version_files = glob.glob("sh_vers*")
#print(sh_version_files)

headers = ["hostname", "ios", "image", "uptime"]

def parse_sh_version(filename):
    result_list = []
    regex = (r'Cisco IOS Software,\s+\S+ \S+\s+\S+, Version (?P<ios>\S+[^ ,])'
             r'|System image file is "(?P<image>\S+)"'
             r'|router uptime is (?P<uptime>\S+ \w+, \d+ \w+, \d+ \w+)')
    match = re.finditer(regex, filename)
    if match:
        for i in match:
            if i.group('ios'):
                result_list.append(i.group('ios'))
            elif i.group('image'):
                result_list.append(i.group('image'))
            elif i.group('uptime'):
                    result_list.append(i.group('uptime'))
    result_list[-1], result_list[1] = result_list[1], result_list[-1]
    return tuple(result_list)

def write_inventory_to_csv(data_filenames,csv_filename):
    list_for_csv = [headers]
    for file in data_filenames:
        hostname = file.split('_')[-1].split('.')[0]
        with open(file) as show_ver_file, \
                open(csv_filename, 'w') as file_for_writing:
            inventory_list = list(parse_sh_version(show_ver_file.read()))
            inventory_list.insert(0,hostname)
            list_for_csv.append(inventory_list)
            writer = csv.writer(file_for_writing)
            writer.writerows(list_for_csv)

if __name__ == '__main__':
    write_inventory_to_csv(sh_version_files,'routers_inventory.csv')
