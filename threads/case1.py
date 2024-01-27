from time import sleep
from threading import Thread
from threading import current_thread
from threading import main_thread

# 获取主线程的两种方式
main_thread1 = main_thread()
print(main_thread1.name, main_thread1.daemon, main_thread1.ident)


main_thread = current_thread()
print(main_thread.name, main_thread.daemon, main_thread.ident)

# run a function in a thread without parameters
def task():
    sleep(2)
    print("This is from another thread.")


thread = Thread(target=task)
print(thread.is_alive())
print(thread.ident)
thread.start()
print(thread.is_alive())
print(thread.ident)
print("Waiting for the thread...")
thread.join() # 把创建的新线程加入到进程中，显示进行阻塞主线程且等待新线程结束执行
print(thread.name)
print(thread.is_alive())

# run a function in a thread with parameters
def task(seconds, message):
    sleep(seconds)
    print(message)


thread = Thread(target=task, args=(3, "New message from another thread."))
thread.start()
print("Waiting for the thread...")
thread.join()
print(thread.name)

# extend thread

class CustomThread(Thread):
    def run(self) -> None:
        sleep(3)
        print("This is coming from another thread.")

thread = CustomThread()

thread.start()
print("waiting for the thread....")
thread.join()
print(thread.name)

