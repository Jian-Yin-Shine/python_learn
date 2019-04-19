# map(fun, iter1, ...)
# 将iter1通过fun映射
# https://docs.python.org/zh-cn/3/library/functions.html#map

# python 2.x 返回一个列表
# python 3.x 返回一个迭代器

def square(x):
    return x**2

print( map(square, [1,2,3,4]) )
for i in map(square, [1, 2, 3, 4]):
    print(i)

for i in map(lambda x : x**2, [1, 2, 3, 4]):
    print(i)

# 也可以传多个参数，只要函数能够处理, 在短的时候停止

for i in map(lambda x, y : x+y, [1, 2, 3], [1, 2, 3, 4]):
    print(i)

# 例子：名字第一个大写，后面都小写

def func(a):
    a = a[:1].upper() + a[1:].lower()
    return a

for i in map(func, ['aBam', 'tree', 'Dream']):
    print(i)
