# -*- coding: utf-8 -*-
"""
Задание 5.1

Создать генератор get_ip_from_cfg, который ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Генератор должен обрабатывать конфигурацию и возвращать кортеж на каждой итерации:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например: ('10.0.1.1', '255.255.255.0')

Для получения такого результата, используйте регулярные выражения.

Проверить работу генератора на примере файла config_r1.txt.

"""
import re


def get_ip_from_cfg(filename):
    with open(filename, 'r') as f:
        regex = re.compile(r'interface.+?ip.+?(\d+\.\d+\.\d+\.\d+)\s(\d+\.\d+\.\d+\.\d+)', re.DOTALL)
        match = re.findall(regex, f.read())
        for item in match:
            yield item
    
    
if __name__ == '__main__':
    gen = get_ip_from_cfg('config_r1.txt')
    for i in gen:
        print(i)
