# 实例属性self. 和类属性

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print("Hello , i am ", self.name)

        
# p1 = Person('Tree', 22)
# p1.say()
# print(p1.age)

# 类属性
class Person2:
    count = 0  # 类属性
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person2.count +=1
    
    def __del__(self):
        Person2.count-=1
    
    def say(self):
        print("Hello, i am", self.name)
    
    def get_count():
        print("The sum count is ", Person2.count)

        
# p21 = Person2("tree", 21)
# p22 = Person2("dream",21)
# Person2.get_count()
# del p21
# Person2.get_count()


# 私有属性 and 公有属性
# __属性不可访问，可以在方法中访问
class A:
    __name2 = 'tree'
    def __init__(self):
        self.name = '1'
        self.age = 1
        self.__name = '2'
    def get_name(self):
        print(self.__name, A.__name2)