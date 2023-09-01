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
