from multiprocessing.pool import ThreadPool
from time import sleep
from random import random, randint


def task(id):
    value = randint(1, 10)
    sleep(value)
    return id,value

def progress(results):
    print(".",results, end="", flush=True)

if __name__ == "__main__":
    with ThreadPool() as pool:
        results = [pool.apply_async(func=task, args=(i,), callback=progress) for i in range(20)]
        pool.close()
        pool.join()
    res = [e.get() for e in results]
    print()
    print(res)