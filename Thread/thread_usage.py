import threading,time,random

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(5):
            time.sleep(1)
            t = threading.currentThread()
            print('{0} at {1}\n'.format(t.name,time.ctime()))
        print(f'线程{threading.currentThread().name}结束')

def test():
    t1 = MyThread()
    t1.name='t1'
    t1.start()
    print('主线程开始等待线程（t1）2s')
    t1.join(2)
    print('2s结束\n')
    print('主线程等待，直至t1线程')
    t1.join()
    print('主线程结束')

if __name__ == '__main__':
    test()
