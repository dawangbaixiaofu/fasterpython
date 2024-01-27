from multiprocessing import Process
from time import sleep


def task():
    sleep(80)
    print("this is from another process.")

if __name__ == "__main__":
    process = Process(target=task)
    process.start()
    print("waiting for the process...")
    process.join()