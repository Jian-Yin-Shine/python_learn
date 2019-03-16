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

# 参数传递，（值传递，引用传递）
def fun(a):
    a = 10
b = 2
fun(b)
# 有int对象2，指向它的变量是b，传给函数时，按传值的方式复制了变量b，a,b同时指向2
# a = 10 ，新建一个int对象 10, a指向它，所以b不变

def fun(mylist):
    mylist.append([1,2,3,4])
    print(mylist)

ls = [10,20]
fun(ls)
# [10, 20, [1, 2, 3, 4]]
>>> ls
# [10, 20, [1, 2, 3, 4]]


def fun(ls=[])
    ls.append('end')
    print(ls)
    
fun()
# ['end']
fun()
# ['end', 'end']
# 第一次调用ls 变量指向对象 [],然后增加‘end’，此时对象[]已经修改，下一次调用fun，ls指向的对象已经被修改了

# modify
def fun(ls=None):
    if ls==None:
        ls = []
    ls.append('end')
    print(ls)




# 匿名函数
ums = lambda arg1, *arg2 : arg1 + sum(arg2)
sums(1,1,2)





