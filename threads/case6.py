from threading import Condition, Thread
from time import sleep


def task(condition:Condition, worklist):
    sleep(2)
    worklist.append(33)
    print("Thread sends notification...")
    with condition:
        condition.notify()
        sleep(2)
        print("has send the message")


condition = Condition()
worklist = list()


with condition:
    thread = Thread(target=task, args=(condition, worklist))
    thread.start()
    condition.wait()
    
print(f"receive the message, and the data is {worklist}")