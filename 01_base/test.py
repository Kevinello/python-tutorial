from datetime import time
from multiprocessing import Process
import os
from time import sleep

# 子进程要执行的代码
def run_proc(name):
    print(f'Run child process {name} ({os.getpid()})...' )
    sleep(5)
    print(f'Child process {name} ({os.getpid()}) end.' )

if __name__=='__main__':
    print(f'Parent process {os.getpid()}.')
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Parent process end.')