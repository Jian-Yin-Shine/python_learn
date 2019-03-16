# python 传参

def my_sum(a, b):
    print(a,b)
    return a+b

print(my_sum(1,2))

# 可选参数（默认参数）放到最后
def my_sum_c(a, b=1):
    print(a, b)
    return a+b

print(my_sum_c(5))

# 位置参数：传参时，默认按照位置传递
# 命名参数：可以指定命名参数
# * 后面必须是命名参数，传递时必须带名字 （例如：def fun(init=5, *, a, b)，a必须是带名字

def fun(init=5, *, ves, vess):
    print(init, ves, vess)

fun(ves=[1,2,3], vess={'a':1, 'b':2})
fun(init=3, ves=1, vess= {'a':1, 'b':2})


# 可变参数
def fun(a, *args):
    print(a, args)
    sum = 0
    for i in args:
            sum+=i
    print(sum)

fun(1, 1, 2, 3)


def fun(*arg1, **vardict):
    print(arg1, vardict)
    for i in arg1:
        print(i)
    for i in vardict:
        print(i, vardict[i])
fun(1,2,3,a=1,b=2)


# 匿名函数
ums = lambda arg1, *arg2 : arg1 + sum(arg2)
sums(1,1,2)    


