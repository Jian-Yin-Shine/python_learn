
# eval() 主要用于动态表达式值
x = 2
str = input()
# x**2 + 2
print(eval(str))


# exec() 主要用于执行动态语句
str = input()
# for i in range(10): print(i, end=' ')
exec(str)

# compile，将代码编译为代码对象
# compile(source, filename, mode) mode:编译模式，exec执行，eval 求值，single单个交互语句
co = compile('for i in range(10): print(i)', '', 'exec')
print(co)
exec(co)