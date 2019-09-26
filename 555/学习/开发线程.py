# # 同步编程和异步编程
# # 异步编程 加入了多线程
import time
import threading

def asd():
    time.sleep(4)
    print(time.time())
    print('6666')

def ad():
    time.sleep(2)
    print(time.time())
#同步编程。
ad()
asd()
#异步编程 加入了多线程
threading.Thread(target=ad).start()
threading.Thread(target=asd).start()
#方式一
# from threading import Thread
# import time
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     t=Thread(target=sayhi,args=('egon',))
#     t.start()
#     print('主线程')



# #     aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#
# import threading
# import time
#
# def sayhi(name):
#     time.sleep(2)
#     print('%s say hello' %name)
#
# if __name__ == '__main__':
#     threading.Thread(target=sayhi,args=('egon',)).start()
#     print('主线程')
#




















