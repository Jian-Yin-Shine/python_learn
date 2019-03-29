# 全局变量：在函数，类定义以外，和 import 进来的变量

# 全局语句 global
g = 123
def fun():
    g = 234
    print(g)

g
# 123
fun()
# 234
g
# 123

def fun():
    global g
    g = 234

g
#123
fun()
g
# 234


# 非局部语句 nonlocal
# 在函数体中，可以嵌套函数，
# nonlocal 使用上层函数中定义的局部变量
def fun():
    a = 0.7
    print(a)
    def fun_in():
        nonlocal a
        a = 0.5
        print(a)
    fun_in()
    print(a)

fun()
# 0.7
# 0.5
# 0.5
