'''
牛客网python专项练习
'''
# 1. map
# https://github.com/Jian-Yin-Shine/python_learn/blob/master/module/st_map.py
a = map(lambda x : x**3, [1, 2, 3])
print(list(a))


# 5. 关于全局变量和局部变量
# 下列代码执行结果是什么？
'''
x = 1
def change(a):
    x +=1
    print(x)
change(x)
'''
# 答案是报错
# 补充：如果change()里面是访问x 而不是修改，则操作是合法的。

x = 1
def change(a):
    a += x
    print(a)
change(x)

# 补充二：
# https://github.com/Jian-Yin-Shine/python_learn/blob/master/language/st_var_area.py

# 要修改全局变量时，使用global ，嵌套函数时，使用类似global的nonlocal

# 7. python 2,3 均不支持复数比较大小

