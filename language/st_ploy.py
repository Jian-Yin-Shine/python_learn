# python 多态性

class Animal(object):
    def run(self):
        print('Animal is running ... ...')
        

class Dog(Animal):
    pass

class Cat(Animal):
    pass


# 通过继承，继承基类所有非私有的属性和方法
dog = Dog()
dog.run()

cat = Cat()
cat.run()


# 定义自己的方法，覆盖父类
class Dog(Animal):
    def run(self):
        print("Dog is running ... ...")
        
        
class Cat(Animal):
    def run(self):
        print("Cat is running ... ...")
        
dog = Dog()
dog.run()
cat = Cat()
cat.run()


# 多态
def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


# 新增了一个子类
# 但是我们不需要修改run_twice方法，run_twice方法只需要
# 接收Animal类型就可以了。


# 即多态：对于一个变量，只需要知道他是Animal类型，无需确切知道他的子类型
# 就可以放心调用run方法，而具体调用的是Animal, Dog, Cat, 还是Tortoise的run方法
# 看具体运行时该对象类型决定。

# 当新增一个Animal 子类，只要确保run()方法编写正确，不需要管原来的代码是如何调用。这也是著名的开闭原则。
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly... ...')
        
run_twice(Tortoise())        
        
        
        
        
        
        