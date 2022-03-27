# colors = ['red', 'green', 'blue']  # Источник данных в нашем случае список
# data = open('file.txt', 'a')       # Указываем имя файла и мод с которысм работаем 
# # data.writelines(colors)          # Разделителей не будет 
# data.write('\nLine 12\n')
# data.write('Line 13\n')  
# data.close()                       # Разрыв соединения с файлом
# --------------------------------------------------------------------------------------
# with open('file.txt', 'w') as data:
#     data.write('Line 2')
#     data.write('\nLine 3')
# ======================================================================================
# path = 'file.txt'                    # Путь к нашему файлу
# data = open(path, 'r')               # Чтение файла
# for line in data:
#     print(line)
# data.close()
# ======================================================================================
# import function as func              # Импортируем файл function
# print(func.f(2.3))                   # Вызываем функцию 
# --------------------------------------------------------------------------------------
# def concatenatio(*param):            # Задали функцию
#     res: str = ''                    
#     for item in param:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))
# ======================================================================================
# КОРТЕЖИ
# a = 3, 4
# print(a)
# print(a[0])
# print(a[-1])
# a[0] = 12
# t = ()
# print(type(t))
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 3, 12)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors)
# t = tuple(colors)
# print(t)
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r: {}, g: {}, b: {}'.format(red, green, blue))
# ======================================================================================
# СЛОВАРИ
# dictionary = {}
# dictionary = \
#     {
#         'up': '↑',
#         'left': '←',
#         'down': '↓',
#         'right': '→'
#     }
# print(dictionary)

# for k in dictionary.values():
#     print(k)
# ======================================================================================
# МНОЖЕСТВА
# colors = {'red', 'green', 'blue'}
# print(type(colors))
# colors.add('red')
# print(colors)
# colors.add('gray')
# print(colors)
# colors.remove('red')
# print(colors)
# colors.discard('red')
# print(colors)
# colors.clear()
# print(colors)
# a = {1,  2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)
# dr = b.difference(a)
# print(dr)
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)
# s = frozenset(a)
# =======================================================================
# СПИСКИ
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
# list1[0] = 123
# list2[1] = 333
# for e in list1:
#     print(e)
# print()
# for e in list2:
#     print(e)
# print(len(list1))
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# print(list1.pop())
# print(list1)
# =======================================================================