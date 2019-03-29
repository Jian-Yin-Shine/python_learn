# __init__, __del__ 之前有使用过了，注意__init__不需要return, __del__ python解释器实现自动垃圾回收，即无法保证这个方法什么时候运行,可以强制销毁
# __init__方法，构造方法
# __new__方法，创建对象时调用，返回当前对象的一个实例，一般不需要重载
# 类方法，静态方法的区别，参数不一样
# 都不能访问对象实例属性，或者对象实例
# 都可以通过类访问和实例访问
# https://www.cnblogs.com/wcwnina/p/8644892.html

class ClassTest():
    __num = 0
    
    @classmethod
    def addNum(cls):
        cls.__num+=1
    
    @classmethod
    def getNum(cls):
        return cls.__num
    
    
class Student(ClassTest):
    def __init__(self):
        self.name = ""
        
a = Student()
b = Student()
print(ClassTest.getNum())


import time
class TimeTest:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    @staticmethod
    def showTime():
        return time.strftime("%H:%M:%S",time.localtime())

    
print(TimeTest.showTime())
t = TimeTest(2, 10, 10)
nowTime = t.showTime()
print(nowTime)

# 私有方法 and 公有方法 同属性__
