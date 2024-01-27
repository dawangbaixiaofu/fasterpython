from threading import Thread, RLock, Lock
from time import sleep
from random import randint



def report(lock, identifier):
    with lock:
        print(f"> thread-{identifier} is done")


def task(lock, identifier, value):
    with lock:
        print(f"> thread-{identifier} sleep {value} seconds.")
        sleep(value)
        report(lock, identifier)

lock = RLock()
# lock = Lock() # if the lock is not a reenterance then will be a dead lock state.

for i in range(1, 11):
    Thread(target=task, args=(lock, i, randint(1, 5))).start()