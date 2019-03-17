# @functools.wraps装饰器
# http://www.runoob.com/w3cnote/python-func-decorators.html

# 装饰器会重写函数的名字和注释文档，wraps就是防止这个问题

# import functools

# def decorator_name(func):
#     @functools.wraps(func)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run"
#         return func(*args, **kwargs)
#     return decorated

# @decorator_name
# def func():
#     return ("Function is running")

# can_run = True
# print(func())

# can_run = False
# print(func())


import time, functools

def foo(func):
    """ foo function Docstring"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """ wrapper function Docstring"""
        print('调用函数：',func.__name__)
        return func(*args, **kwargs)
    return wrapper


@foo
def bar(x):
    """bar function Docstring"""
    return x**2

# if __name__ == '__main__':
#     print(bar(2))
#     print(bar.__name__)
#     print(bar.__doc__)
    
# functools.update_wrapper有同样的功能


# 日志，日志本身需要参数，高阶函数产生
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000


def log(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log(str(time.time()))
def now():
    print('xxxxx')
    
now()
# now = log('time.time()')(now)
# now() : 先执行log('time.time()') 返回decorator函数名，参数是now,执行它，返回wrapper，参数是 *args, **kwargs，这样，这里就可以写日志文件了
    
    
    