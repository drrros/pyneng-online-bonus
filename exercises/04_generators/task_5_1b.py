# -*- coding: utf-8 -*-
"""
Задание 5.1b

Переделать генератор get_intf_ip из задания 5.1a таким образом,
чтобы он принимал как аргумент любое количество файлов.

Генератор должен обрабатывать конфигурацию и возвращать словарь
для каждой конфигурации на каждой итерации:
* ключ - hostname
* значение словарь, в котором:
    * ключ - имя интерфейса
    * значение - кортеж с IP-адресом и маской

Например: {'r1': {'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
                  'FastEthernet0/2': ('10.0.2.2', '255.255.255.0')}}

Проверить работу генератора на примере конфигураций config_r1.txt и config_r2.txt.

"""
import re
from pprint import pprint


def get_intf_ip(filenames):
    for filename in filenames:
        with open(filename, 'r') as f:
            device = filename.split('.')[0].split('_')[1]
            regex = re.compile(r'interface\s(\S+).+?(?:(?:ip\saddress.+?(\d+\.\d+\.\d+\.\d+)\s(\d+\.\d+\.\d+\.\d+))|(?:no\sip\saddress)|(?:!))', re.DOTALL)
            match = re.finditer(regex, f.read())
            for item in match:
                if item.groups()[1]:
                    yield {device: {item.groups()[0]: (item.groups()[1], item.groups()[2])}}


if __name__ == '__main__':
    gen = get_intf_ip(['config_r1.txt', 'config_r2.txt'])
    for i in gen:
        pprint(i)
