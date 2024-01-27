from random import randint
from time import sleep
from threading import Thread, Lock


def task(lock:Lock, identifier:int, value):
    with lock:
        print(f"Thread-{identifier} got the lock, sleep for {value} seconds.")
        sleep(value)

lock = Lock()

for i in range(1, 11):
    Thread(target=task, args=(lock, i, randint(1, 10))).start()