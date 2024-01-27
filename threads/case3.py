from time import sleep
from threading import local, Thread




def task(value):
    l = local()
    l.value = 5 
    print("Before changing local value, its' value is: ", l.value)
    l.value = value
    sleep(value)
    print("After changing local value, its' value is: ")
    print(f"Stored value: {l.value}")


thread1 = Thread(target=task, args=(9,))
thread1.start()

thread2 = Thread(target=task, args=(4,))
thread2.start()
