
def decorator5(func):
    #print('Запускаем decorator5')
    def inner(*args, **kwargs):
        print('Вызываем', func.__name__)
        return func(*args, **kwargs)
    return inner


@decorator5
def multiply(a, b):
    return a*b


@decorator5
def mysumm(*args):
    return sum(args)

if __name__ == '__main__':
    multiply(3,4)
    mysumm(1,2,3,4)

