# -*- coding: utf-8 -*-
"""
Задание 5.1a

Создать генератор get_intf_ip, который ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Генератор должен обрабатывать конфигурацию и возвращать кортеж на каждой итерации:
* первый элемент кортежа - имя интерфейса
* второй элемент кортежа - IP-адрес
* третий элемент кортежа - маска

Например: ('FastEthernet', '10.0.1.1', '255.255.255.0')

Для получения такого результата, используйте регулярные выражения.

Проверить работу генератора на примере файла config_r1.txt.
"""
import re


def get_intf_ip(filename):
    with open(filename, 'r') as f:
        regex = re.compile(r'interface\s(\S+).+?(?:(?:ip\saddress.+?(\d+\.\d+\.\d+\.\d+)\s(\d+\.\d+\.\d+\.\d+))|(?:no\sip\saddress)|(?:!))', re.DOTALL)
        match = re.finditer(regex, f.read())
        for item in match:
            if item.groups()[1]:
                yield item.groups()


if __name__ == '__main__':
    gen = get_intf_ip('config_r1.txt')
    for i in gen:
        print(i)
