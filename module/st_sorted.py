# python 排序


# list.sort() 无返回值，直接原地排序，稳定排序，无法对字典排序
# https://docs.python.org/zh-cn/3/library/stdtypes.html?highlight=sort#list.sort
ls = [1, 2, 3, 4, 3, 2, 1]
print(ls)
ls.sort()
print(ls)

# sorted() 排序, 返回一个新的list，稳定排序
ls = [1, 2, 3, 4, 3, 2, 1]
a = sorted(ls)
print(ls , a)


# sorted(*, key=None, reverse=False)
# https://docs.python.org/zh-cn/3/library/functions.html#sorted
# 参数只能通过关键字参数传递，及定义时： def sorted(iter, *, arg1, arg2): pass

# sorted 默认对字典健排序
dicts = {'b': 1, 'a': 2}
print(sorted(dicts))

# for i in sorted(dicts):
#     print(dicts[i])

# key 参数为一个函数： 该函数只有一个参数，返回一个值
# 在每次比较两个元素时调用，将比较的元素放到这个函数中，及可以完成重载操作符
print(sorted(dicts, key=lambda x:dicts[x]))

student_tuple = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

print(sorted(student_tuple, key= lambda x:x[2]))

# 现在我来自定义数据结构 class
# https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    # 重载str()函数
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

    # 排序时使用key，或者操作符重载 <
    # Student.__lt__ = lambda self, other : self.grade < other.grade
    def __lt__(self, other):
        return self.grade < other.grade


student_objs = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

# 按照年龄排序
print(sorted(student_objs, key=lambda x:x.age))
print(sorted(student_objs))