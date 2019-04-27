# import threading, time, random

# 自定义用户进程类，实现run()方法
# 通过创建其对象实例，来创建线程，启动线程
'''
class MyThread(threading.Thread) :
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval

    def run(self):
        for i in range(5):
            time.sleep(random.choice(range(self.interval)))
            thread_id = threading.get_ident()
            print ('Thread: {0} Time : {1}'.format(thread_id, time.ctime()))



if __name__ == '__main__':
    t1 = MyThread(5)
    t2 = MyThread(5)
    t1.start()
    t2.start()
'''
#  join() 方法： t.join() 将一个线程加到另外一个线程的尾部，等待线程 t 完成，或者超时
'''
import threading, time, random

class MyThead(threading.Thread):
    def __int__(self):
        threading.Thread.__init__(self)
    def run(self):
        for i in range(5):
            time.sleep(1)
            t = threading.current_thread() # 获取当前线程
            print ('{0} at {1}'.format(t.name, time.ctime()))
        print('线程t1结束')

def test():
    t1 = MyThead()
    t1.name ='t1'
    t1.start()
    t1.join(3)
    for i in range(200):
        print (i)

    print('等待结束')

if __name__ == '__main__':
    test()
'''

# 线程同步
# 原语锁 Lock
# 关键代码放到 acquire(), release()之间
# import threading
# lock = threading.Lock()
# lock.acquire()
# ...
# lock.release()

# 银行账户余额同步
# 多个线程调用单个对象的属性和方法时， 一个线程可能中断另一个线程正在进行的任务，使得变量处于混乱的
# 使用锁来同步
import threading, time, random
class Account(threading.Thread):
    lock = threading.Lock()
    def __init__(self, amount):
        threading.Thread.__init__(self)
        Account.amount = amount

    def run(self):
        self.withdraw()

    def withdraw(self):
        Account.lock.acquire()  # 获取锁
        t = threading.current_thread()
        a = random.choice(range(50, 101))
        if Account.amount < a:
            print ('{0} 交易失败。提取前余额：{1}, 取款额:{2}'.format(t.name, Account.amount, a))
            Account.lock.release()
            return 0
        time.sleep(random.choice(range(5)))
        pre = Account.amount
        Account.amount -= a
        print ('{0} 取款前余额: {1}, 取款额: {2}, 取款后额: {3}'.format(t.name, pre, a, Account.amount))
        Account.lock.release()

def test():
    for i in range(5):
        Account(200).start()

if __name__ == '__main__':
    test()