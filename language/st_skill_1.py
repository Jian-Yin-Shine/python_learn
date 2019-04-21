# 经常看到的所谓的python 8个技巧

# 1. 条件
condition = True
'''
condition = True
if condition:
    x = 1
else :
    x = 2
print(x)'''

x = 1 if condition else 2
print(x)

# 2. 大数字分割
num1 = 10_000_000_000
num2 = 100_000_000
print(num1 + num2)

# 3. 文件关闭
# open创建文件对象
# 读取有两种，for 循环
# read()方法
'''
file = open('st_call.py', 'r')
file_contents = file.read()
file.close()

words = file_contents.split()
word_count = len(words)
print(word_count)'''

with open('st_call.py', 'r') as f:
    # for line in f:
    #     print(line)
    file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    print(word_count)

# 4. enumerate 下标
names = ['aaa', 'bbbb', 'ccc']
for index, name in enumerate(names):
    print(index, name)


# 5. 遍历多个列表 zip
names = ['aaa', 'bbb', 'ccc']
ages = [12, 11, 13]
habits = ['sport', 'dance']

for name, age, habit in zip(names, ages, habits):
    print(name, age, habit)

# 6. 分解变量 *_, *mid
# st_*args.py
nums = (1, 2, 3, 4, 5)
head, *midles, tail = nums
print(head, midles, tail)

# 7. setattr函数


# 8. 加密的密码 getpass

username = input('username: ')
passwd = input('Passwd: ')
from getpass import getpass
passwd = getpass('Passwd: ')