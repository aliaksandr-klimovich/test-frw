import threading
import time

class TestCase:
    def run(self):
        pass

class MyTestCase(TestCase):
    def run(self):
        print('start')
        time.sleep(3)
        print('end')

if __name__ == '__main__':
    my_test_case = MyTestCase()
    thread = threading.Thread(
        target=my_test_case.run,
    )
    thread.start()
    time.sleep(1)
    # thread.kill()
    thread.join()
