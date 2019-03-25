#定义了__call__方法的对象，称为可调用对象，该对象可以像函数一样被调用

# 自由落体 h = 1/2 g tˆ2

class GDistance:
	def __init__(self, g):
		self.g = g
	def __call__(self, t):
		return (self.g*t**2)/2

if __name__=="__main__":
	g = GDistance(9.8)
	for i in range(11):
		print("%f "% g(i))
