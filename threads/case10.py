from threading import Thread, Event
from time import sleep


def task(event:Event):
    for i in range(5):
        sleep(1)
        if event.is_set():
            break
        print("this new thread's task is working.")
    print("this work in new thread is terminated.")

event = Event()
work = Thread(target=task, args=(event, ))
work.start()

sleep(3)

event.set()
print("stopping new thread wihtin main thread")
work.join()
