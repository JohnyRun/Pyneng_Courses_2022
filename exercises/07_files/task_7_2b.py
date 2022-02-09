# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ignore = ["duplex", "alias", "configuration"]

file_conf = argv[1]
result_conf = argv[2]

with open(file_conf) as file, open(result_conf, 'w') as dest:
    for line in file:
        flag = False
        if not "!" in line:
            for ignore_word in ignore:
                if ignore_word in line:
                    flag = True
            if not flag:
                dest.write(line.rstrip())
                dest.write('\n')