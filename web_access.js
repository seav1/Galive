import time
import sched
from xvfbwrapper import Xvfb
from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_basic(self):
        self.open('https://ide-run.goorm.io/workspace/dGz54pALkYySfIqjBmp?token=ce166f5eccf285db2d818ed4c65a7c12&guestname=12')
        time.sleep(60)  # 保持1分钟

def run_test():
    with Xvfb() as xvfb:
        test = MyTestClass()
        test.setUp()
        try:
            test.test_basic()
        finally:
            test.tearDown()

scheduler = sched.scheduler(time.time, time.sleep)
def schedule_test():
    scheduler.enter(20*60, 1, run_test, ())  # 每20分钟运行一次
    scheduler.run()

if __name__ == "__main__":
    schedule_test()
