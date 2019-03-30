# @property装饰器将函数当作属性用
# __call__ 将对象当作函数用
class Person:
	def __init__(self, name):
		self.__name = name
	
	@property
	def name(self):
		return self.__name


p = Person('aaa')
p.name

class Person2:
	def __init__(self, name):
		self.__name = name
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value):
		self.__name = value
	
	@name.deleter
	def name(self):
		del self.__name


class Person3:
	def __init__(self, name):
		self.__name = name

	def getname(self):
		return self.__name
	
	def setname(self, value):
		self.__name = value
	
	def delname(self):
		del self.__name

	name = property(getname, setname, delname)

