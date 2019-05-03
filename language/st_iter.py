# python 内置可迭代对象
import itertools

print(list(range(5)))

# 映射，map可以传入一个，或多个迭代器
print(list(map(lambda x: abs(x), (1, -1, 2, -2, 3, -3))))
print(list(map(lambda x, y, z : x+y+z, (1, 2),(3, 4), (5,6))))
print(list(itertools.starmap(lambda x,y,z: x**y+z, [(1, 2, 3), (3, 4, 3)]) ))

# filter筛选满足条件的
print (list(filter(lambda x : x>0, (0, 1, 2, -1, 2))))
print (list(filter(None, ([], {}, 1, 3.2, 'a'))))
print (list(itertools.filterfalse(lambda x: x%2, [0, 1, 2, 3, 4, 5, 6])))

# zip 将多个迭代器重新组合，返回一个元组
print (list(zip([0,1,2], "abcd", 'xyz')))
print (list(itertools.zip_longest([0, 1, 2], "abcd", 'zx', fillvalue="*")))

# index
print (list(enumerate('abxy', start=0)))

# 三个无穷迭代器
print (list(zip('abcd', itertools.count(0))))
print (list(zip(range(10), itertools.cycle('abc'))))
print (list(itertools.repeat('abc', 3)))

# 累加迭代器，可自定义函数
print (list(itertools.accumulate((1,2,3,4), lambda x, y: x * y)))

# 级联迭代器，将多个迭代器依次迭代，而不是像zip一样每个迭代器拿一个返回元组
print (list(itertools.chain('abc', range(5), 'xyz')))
print (list(itertools.chain.from_iterable(['abc', range(5), 'xyz'])))

# compress 相当于np.where
print (list(itertools.compress('abcdefg', [0, 1, 1, 0, 1])))
print (list(itertools.dropwhile(lambda x : x < 5, [0, 1, 2, 3, 4, 5, 6, 0, 1, 2])))
print (list(itertools.takewhile(lambda x : x < 5, [0, 1, 2, 3, 4, 5, 6, 0, 1, 2])))

# groupby 首先要给序列排序，然后返回 key , group
data = [1, -2, 0, 0, -1, 2, 1, -1, 2, 0, 0]
data = sorted(data, key=lambda x:abs(x))

for k, g in itertools.groupby(data, key=lambda x : abs(x)):
    print (k, list(g))

# 无重复元素组合， 重复元素组合
print (list( itertools.combinations([1,2,3], 2)))
print (list( itertools.combinations_with_replacement([1, 2, 3], 3)))

# 全排列
print (list( itertools.permutations([1, 2, 3], 2)))
print (list( itertools.permutations([1, 2, 3])))

# 笛卡尔积
print (list( itertools.product([1, 2], 'abc')))
print (list( itertools.product([1, 2], repeat=3)))