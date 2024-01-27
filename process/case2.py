from collections.abc import Callable, Iterable, Mapping
import ctypes
from multiprocessing import Process, Value
from time import sleep
from typing import Any


typecode_to_type = {
    'c': ctypes.c_char,     'u': ctypes.c_wchar,
    'b': ctypes.c_byte,     'B': ctypes.c_ubyte,
    'h': ctypes.c_short,    'H': ctypes.c_ushort,
    'i': ctypes.c_int,      'I': ctypes.c_uint,
    'l': ctypes.c_long,     'L': ctypes.c_ulong,
    'q': ctypes.c_longlong, 'Q': ctypes.c_ulonglong,
    'f': ctypes.c_float,    'd': ctypes.c_double
    }


class CustomProcess(Process):
    def __init__(self):
        Process.__init__(self)
        self.data = Value('i', 0)
    def run(self):
        sleep(1)
        self.data.value = 90
        print(f"Child stored: {self.data.value}")
    
if __name__ == "__main__":
    process = CustomProcess()
    process.start()
    print(f"Waiting for child process is terminated.")
    process.join()
    print(f"Parent Process got:{process.data.value}")        