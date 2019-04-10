#之前是长度一定，现长度可变的对象分解，*
# *变量分解时，可以放在前面，中间，最后

def drop_first_last(grads):
    first, *middle, last = grads
    return sum(middle)

print( drop_first_last((1,2,3,4,3)) )


recode = ('Dave', '123@gmail.com', '132xxxxxxxx', '136xxxxxxxx')
name, email, *tel = recode
print(tel)

*x, y = recode
print(x)
