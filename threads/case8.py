from threading import Thread, Barrier
from time import sleep
from random import randint


def task(barrier:Barrier, identifier):
    value = randint(1, 5)
    sleep(value)
    print(f"Thread-{identifier} got {value}")
    barrier.wait()
    print(f"Thread-{identifier} synchronized.")


barrier = Barrier(parties=6)
for i in range(5):
    worker = Thread(target=task, args=(barrier, i))
    worker.start()

sleep(randint(1, 5))
print("main thread and other threads do something else and then synchronize all threads, means just begining to do something after main thread and other thread have finished")
barrier.wait()
print("Main Thread synchronized.")
