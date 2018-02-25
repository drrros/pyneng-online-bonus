import logging


def log(func):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def inner(*args, **kwargs):
        logging.debug('Вызываем {}'.format(func.__name__))
        if args:
            logging.debug('\tПозиционные аргументы: {}'.format(args))
        if kwargs:
            logging.debug('\tКлючевые аргументы: {}'.format(kwargs))
        result = func(*args, **kwargs)
        logging.debug('\tРезультат функции: {}'.format(result))
        return result
    return inner


@log
def mult(a,b):
    return a*b

@log
def sub(a,b):
    return a-b


mult(4,5)
mult(a=100, b=300)
sub(100,44)
