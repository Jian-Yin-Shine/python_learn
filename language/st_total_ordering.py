# 操作符可以重载，就是要实现__eq__, __lt__, __le__, __ge__, __gt__等方法
# 使用functools.total_ordering则只需要实现其中之一

import functools

@functools.total_ordering

class Student:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def __eq__(self, other):
		return (self.firstname.lower(), self.lastname.lower()) == \
			(other.firstname.lower(), other.lastname.lower())

	def __lt__(self, other):
		return (self.firstname.lower(), self.lastname.lower()) < \
        	(other.firstname.lower(), other.lastname.lower())
