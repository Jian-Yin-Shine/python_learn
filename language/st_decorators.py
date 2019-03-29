# 装饰器
# https://www.cnblogs.com/lianyingteng/p/7743876.html#undefined
# 实质： 是一个函数
# 参数：是你要装饰的函数名（并非函数调用）
# 返回：是装饰完的函数名（也非函数调用）
# 作用：为已经存在的对象添加额外的功能
# 特点：不需要对对象做任何的代码上的变动


def foo(f):
    def wrapper(*args, **kwargs):
        print('调用函数: ', f.__name__)
        return f(*args, **kwargs)
    return wrapper

@foo
def bar(x):
    return x**2


import time, functools
def timeit(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print('运行时间：', end-start)

    return wrapper


@timeit
def my_calc(n):
    sums = 0
    for i in range(n): sums+=i
    print(sums)

if __name__ == '__main__':
    print(bar(2))
    print(bar.__name__)
    print(bar.__doc__)
    

    my_calc(100000)
    
    