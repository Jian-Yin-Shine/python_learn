# 保存历史记录100条 deque

# 检查一个文本，当可以匹配时，显示最后检查过的n条，然后输出当前匹配行
# yield 返回一个迭代器，迭代器的第二项又是可迭代的对象
from collections import deque

def search(lines, patter, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if patter in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('file.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)
