x = 0
y = 0

def init(a, b):
    '''Инициализация начальных значений \
        двух переменных на строчках 1 и 2'''
    global x                     # То есть x на 8 строчке с этого момента будет является x на 1 строчке 
    global y                     # То есть y на 9 строчке с этого момента будет является y на 2 строчке
    x = a 
    y = b
    
def do_it():
    '''Метод для вычисления суммы'''
    return x + y
 