from threading import Thread, Lock
from time import sleep


def task(identifier, lock1, lock2):
    print(f"Thread-{identifier} begins to work.")
    while True:
        with lock1:
            sleep(0.2)
            print(f"Thread-{identifier} gets the first lock.")
            if lock2.locked():
                print(f"Thread-{identifier} can't get the second lock, give up...")
            else:
                print(f"Thread-{identifier} attempts to get the second lock, and finishs the progress.")
                break

lock1 = Lock()
lock2 = Lock()
work1 = Thread(target=task, args=(1, lock1, lock2))
work2 = Thread(target=task, args=(2, lock2, lock1))
work1.start()
work2.start()

work1.join()
work2.join()
