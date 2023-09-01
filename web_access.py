from xvfbwrapper import Xvfb
from seleniumbase import BaseCase, config

class MyTestClass(BaseCase):
    def setUp(self):
        super().setUp()
        config.set_headless(True)  # 设置无头模式

    def test_basic(self):
        self.open('https://ide-run.goorm.io/workspace/dGz54pALkYySfIqjBmp?token=ce166f5eccf285db2d818ed4c65a7c12&guestname=12')

def run_test():
    with Xvfb() as xvfb:
        test = MyTestClass()
        test.setUp()
        try:
            test.test_basic()
        finally:
            test.tearDown()

if __name__ == "__main__":
    run_test()
