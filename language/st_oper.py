# 操作符重载

class mylist:
    def __init__(self, *args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)
            
    def __add__(self, n):
        for i in range(len(self.__mylist)):
            self.__mylist[i]+=n
    
    def __sub__(self, n):
        for i in range(len(self.__mylist)):
            self.__mylist[i]-=n
            
    def __mul__(self, n):
        for i in range(len(self.__mylist)):
            self.__mylist[i]*=n
    
    def __truediv__(self, n):
        for i in range(len(self.__mylist)):
            self.__mylist[i] /= n
    
    # 重载内置函数len()
    def __len__(self):
        return len(self.__mylist)
    
    # 重载内置函数str()
    def __repr__(self):
        str1 =  ''
        for i in range(len(self.__mylist)):
            str1+= str(self.__mylist[i]) + ' '
        return str1
        
        
        
        