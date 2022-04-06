# def f(x):
#     x**2
# g = f
# print(type(f(1)))
# print(type(g(1)))

# def f(x):
#     return x**2

# g = f 

# print(type(f))
# print(type(g))

# print(type(f(4)))
# print(type(g(4)))

# def calc1(x):
#     return x + 10
# # print(calc1(10))

# def calc2(x):
#     return x * 10
# # print(calc2(10))

# def math(op, x):
#     print(op(x))
    
# math(calc2, 10)
# math(calc1, 10)

# def sum(x, y):
#     return x + y

# def mult(x, y):
#     return x * y

# def calc(op, a, b):
#     print(op(a, b))
#     # return op(a, b)
    
# calc(lambda x, y: x + y + 1, 4, 5)

# list = []
# for i in range(1, 101):
#     # if (i % 2 == 0):
#         list.append(i)
# print(list)

# def f(x):
#     return x**3

# list = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
# print(list)

# li = [x for x in range(1, 21)]
# li = list(map(lambda x: x + 10, li))
# print(li)

# data = list(map(int, '1 2 3'.split()))
# for e in data:
#     print(e)
# print('--')

# for e in data:
#     print(e)

# data = [x for x in range(10)]
# res = list(filter(lambda x: not x % 2 == 0, data))
# print(res)

# user = ['insaf', 'asfa', 'asdfa', 'trye']
# ids = [4, 5, 6, 1, 4]
# data = list(zip(user, ids))
# print(data)

user = ['insaf', 'asfa', 'asdfa', 'trye']
ids = [4, 5, 6, 1, 4]
data = list(enumerate(ids))
print(data)
