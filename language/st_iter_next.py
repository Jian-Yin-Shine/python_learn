# 迭代器和生成器
# 可迭代对象，实现了__iter__()的对象，可以用内置函数iter(obj),调用可迭代对西那个的__iter__()方法，返回一个迭代器
# 序列对象，生成器函数，生成器表达式都是可迭代对象

# 迭代器，实现了__next__()的对象，是迭代器，可以实现对象的迭代循环
# 迭代器协议，迭代器对象必须实现__iter__() 和__next__()，__iter__()返回对象本身，__next__()返回下一个元素

t = (1,2)
t = iter(t) # iter返回可迭代对象的迭代器
next(t)    	# next迭代迭代器元素
next(t)
# next(t)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
for i in iter(t):
	print(i)
# for 循环自动将迭代对象转为迭代器
for i in t:
	print(i)

# 自定义可迭代对象和迭代器
class Fib:
	def __init__(self):
		self.a , self.b  = 0, 1

	def __next__(self):
		self.a, self.b = self.b , self.a + self.b
		return self.a 

	def __iter__(self):
		return self

fib = Fib()
for f in fib:
	if f < 1000:
		print(f, end=' ')
	else:
		break

