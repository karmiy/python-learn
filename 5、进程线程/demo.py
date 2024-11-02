"""不使用多进程"""

# 这个程序中 2 个时间是叠加的，要互相等待
# from random import randint
# from time import time, sleep


# def download_task(filename):
#     print(f"开始下载: {filename}")
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f"{filename}下载完成! 耗费了 {time_to_download} 秒")


# def main():
#     start = time()
#     download_task("Python从入门到住院.pdf")
#     download_task("Peking Hot.avi")
#     end = time()
#     print(f"总共耗费了 {end - start} 秒")


# if __name__ == "__main__":
#     main()

"""Process 多进程"""
# 一个进程里可以多个线程，单核 CPU 系统中，CPU 一次只能处理一个线程
# 多个线程共享了 CPU 的执行时间，所以不会减少总时间，可以理解成 CPU 一会处理这个一会处理那个

# 这个程序中 2 个时间可以视为 “并行”，结果是以大的那个为主
# sleep 模拟的 I/O 输出
#   I/O 操作实际上不是由 CPU 直接处理的，而是由专门的硬件
#   CPU 在发起 I/O 请求后，会等待硬件设备完成数据传输。这段等待时间通常称为阻塞时间
#   等待期间，CPU 可以切换去执行其他任务，而不必闲置等待数据返回
#   所以这时 CPU 可以去处理另外那个进程，达到 “并行”

# Process 创建进程

# from multiprocessing import Process
# from os import getpid
# from random import randint
# from time import time, sleep


# def download_task(filename):
#     print(f"启动下载进程，进程号 {getpid()}")
#     print(f"开始下载: {filename}")
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f"{filename}下载完成! 耗费了 {time_to_download} 秒")


# def main():
#     start = time()
#     p1 = Process(target=download_task, args=("Python从入门到住院.pdf",))
#     # start方法用来启动进程
#     p1.start()
#     p2 = Process(target=download_task, args=("Peking Hot.avi",))
#     p2.start()
#     # join方法表示等待进程执行结束
#     p1.join()
#     p2.join()
#     end = time()
#     print(f"总共耗费了 {end - start} 秒")


# if __name__ == "__main__":
#     main()

"""进程独立内存空间"""
# 每个进程有独立内存空间
# 这个程序中 2 个进程会各输出 10 次
# 创建进程的时候，子进程复制了父进程及其所有的数据结构，每个子进程有自己独立的内存空间，各有一个 counter 变量

# from multiprocessing import Process
# from time import sleep

# counter = 0


# def sub_task(string):
#     global counter
#     while counter < 10:
#         print(string, end="\n", flush=True)
#         counter += 1
#         sleep(0.01)


# def main():
#     Process(target=sub_task, args=("Ping",)).start()
#     Process(target=sub_task, args=("Pong",)).start()


# if __name__ == "__main__":
#     main()

"""Thread 多线程"""
# Thread 创建线程
# from random import randint
# from threading import Thread
# from time import time, sleep


# def download_task(filename):
#     print(f"开始下载: {filename}")
#     time_to_download = randint(5, 10)
#     sleep(time_to_download)
#     print(f"{filename}下载完成! 耗费了 {time_to_download} 秒")


# def main():
#     start = time()
#     t1 = Thread(target=download_task, args=("Python从入门到住院.pdf",))
#     t1.start()
#     t2 = Thread(target=download_task, args=("Peking Hot.avi",))
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print("总共耗费了%.3f秒" % (end - start))


# if __name__ == "__main__":
#     main()

# 优化上述代码
# from random import randint
# from threading import Thread
# from time import time, sleep


# class DownloadTask(Thread):  # 继承
#     def __init__(self, filename):
#         super().__init__()
#         self._filename = filename

#     # 重新 Thread 的 run 函数
#     # Thread start 时会创建线程、自动执行 run（原本的 run 是会执行 target 传进来的函数）
#     def run(self):
#         print(f"开始下载: {self._filename}")
#         time_to_download = randint(5, 10)
#         sleep(time_to_download)
#         print(f"{self._filename}下载完成! 耗费了 {time_to_download} 秒")


# def main():
#     start = time()
#     t1 = DownloadTask("Python从入门到住院.pdf")
#     t1.start()
#     t2 = DownloadTask("Peking Hot.avi")
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print("总共耗费了%.3f秒" % (end - start))


# if __name__ == "__main__":
#     main()

"""多线程共享变量（锁）"""
# 通过 “锁” 来保护 “临界资源”，只有获得 “锁” 的线程才能访问 “临界资源”
# 没有得到 “锁” 的线程只能被阻塞起来，直到获得 “锁” 的线程释放了 “锁”

# from time import sleep
# from threading import Thread, Lock


# class Account(object):

#     def __init__(self):
#         self._balance = 0
#         self._lock = Lock()

#     def deposit(self, money):
#         # 先获取锁才能执行后续的代码
#         self._lock.acquire()
#         try:
#             new_balance = self._balance + money
#             sleep(0.01)
#             self._balance = new_balance
#         finally:
#             # 在 finally 中执行释放锁的操作保证正常异常锁都能释放
#             self._lock.release()

#     @property
#     def balance(self):
#         return self._balance


# class AddMoneyThread(Thread):

#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money

#     def run(self):
#         self._account.deposit(self._money)


# def main():
#     account = Account()
#     threads = []
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     for t in threads:
#         t.join()
#     print(f"账户余额为: ￥{account.balance} 元")


# if __name__ == "__main__":
#     main()

"""开发时是否考虑多进程/线程"""
# 论是多进程还是多线程，只要数量一多，效率会上不去
#   切换任务是有代价的（保存当前环境，准备新环境），虽然切换快，但也要耗时，数量一多系统就一直在忙着切任务
# 【不适合】计算密集型：
#   进行大量的计算，消耗 CPU 资源，比如对视频进行编码解码或者格式转换等等
#   这种任务全靠 CPU 的运算能力，任务越多，花在任务切换的时间就越多，CPU 执行任务的效率就越低
# 【适合】I/O 密集型任务：
#   CPU 消耗很少，任务的大部分时间都在等待 I/O 操作完成（因为 I/O 的速度远远低于 CPU 和内存的速度）
#   启动多任务，就可以减少 I/O 等待时间从而让 CPU 高效率的运转
