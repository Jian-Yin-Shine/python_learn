# 将序列分解为单独的变量
p = (4, 5)
x, y = p
print(x,y)

data = ['ACME', 50, (2019, 4, 10)]
name, price, date = data
print(name, price, date)

# 经常使用_作为丢弃的值
_, _, date = data
print(_, date)

