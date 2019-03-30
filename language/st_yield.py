# 在函数中也可以返回迭代器，用yield代替return, 这个函数就是生成器函数

def generater(n):
	for i in range(n):
		yield i*3

a = generater(10)
a = iter(a)
for i in a:
	print(i, end=' ')

# 自定义可迭代对象中__iter__()返回正向可迭代对象
# __reversed__()返回反向可迭代对象, 就可以使用内置函数reversed()函数

class Countdown:
	def __init__(self, start):
		self.start = start

	def __iter__(self):
		n = self.start
		while n > 0:
			yield n
			n -=1

	def __reversed__(self):
		n = 1
		while n <= self.start:
			yield n
			n +=1

a = Countdown(10)
for i in a :
	print(i, end=' ')

for i in reversed(a):
	print(i, end=' ')
