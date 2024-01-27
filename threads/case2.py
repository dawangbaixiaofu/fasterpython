from time import sleep
from threading import Thread
import threading


def task():
    print("Working.....")
    sleep(3)
    raise Exception("Something is wrong!")

def custom_hook(args):
    print(f"Thread failed: {args.exc_value}")

threading.excepthook = custom_hook

thread = Thread(target=task)
thread.start()
thread.join()
print("Countinuing on...")
