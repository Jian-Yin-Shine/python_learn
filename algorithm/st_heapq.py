# heapq 找到最大，最小的N个元素，堆
import heapq

nums = [1,2,9,3,5,5,7]

print(heapq.nlargest(4, nums))
print(heapq.nsmallest(4, nums))

# nlargest最大的n个
# eq sorted(iterable, key=key, reverse=True)[:n]

# 自定义key，lambda匿名函数, lambda arg1, arg2 : sum(arg1, arg2)
portfolio = [
    {'name':'IBM', 'price':100},
    {'name':'Dell', 'price':90},
    {'name':'mac', 'price':120}
]

print(heapq.nlargest(2, portfolio, key= lambda s : s['price']))
