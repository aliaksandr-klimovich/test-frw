from multiprocessing import Process, Queue
import time
import os
from typing import Type


class TestCase:
    def run(self, q):
        pass


class MyTestCase(TestCase):
    def run(self, queue: Queue):
        print('pid:', os.getpid())
        queue.put([1, 2, 3])
        print('sleep 2s')
        time.sleep(2)
        print('after 2s of sleep')


if __name__ == '__main__':
    my_test_case = MyTestCase()
    queue = Queue()
    proc = Process(
        target=my_test_case.run,
        args=(queue,)
    )
    proc.start()
    time.sleep(1)
    print('pid:', proc.pid)
    res = queue.get()
    print(res)
    #time.sleep(1)
    #proc.terminate()
    proc.join()
