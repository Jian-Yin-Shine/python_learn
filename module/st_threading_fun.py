import threading

# threading 可以用于指定函数, 创建一个线程来执行该函数
# threading.Thread 对象的属性，方法有：
# threading.Thread.name
# threading.Thread.is_alive()
# threading.Thread.ident
# threading.Thread.start()
#
# threading.current_thread()   # 返回当前线程
# threading.active_count()     # 当前存活的线程数目
# threading.enumerate()        # 返回活动线程的列表


import threading, time, random

def timer(interval):
    for i in range(5):
        time.sleep(random.choice(range(interval)))
        thread_id = threading.get_ident()
        print ('Thread: {0} Time : {1} '.format(thread_id, time.ctime()))

def test():
    t1 = threading.Thread(target=timer, args=(3,))
    t2 = threading.Thread(target=timer, args=(5,))
    t1.start()
    t2.start()

if __name__ == '__main__':
    test()