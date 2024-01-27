from multiprocessing.pool import ThreadPool
from time import sleep
from random import random



def task1(identifier):
    value = random()
    sleep(value)
    print(f"> {identifier} generates {value}")
    return identifier, value


def task2(identifier, res):
    value = random()
    sleep(value)
    print(f"> {identifier} with {res}, genereates {value}")
    return identifier, res, value



def result_callback(iterable_result):
    for i, v in iterable_result:
        if v > 0.5:
            _ = pool.apply_async(task2, args=(i, v))

if __name__ == "__main__":
    with ThreadPool() as pool:
        result = pool.map_async(task1, range(10), callback=result_callback)
        # wait for all tasks to complete then get result and issue follow-up tasks
        result.wait()
        # close pool
        pool.close()
        # wait for follow-ups tasks to finish
        pool.join()
    