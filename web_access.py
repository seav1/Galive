from seleniumbase import BaseCase, config

class MyTestClass(BaseCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        config.set_headless_browser(True)  # 设置无头模式

    def test_basic(self):
        self.open('https://ide-run.goorm.io/workspace/dGz54pALkYySfIqjBmp?token=ce166f5eccf285db2d818ed4c65a7c12&guestname=12')

def run_test():
    test = MyTestClass()
    try:
        test.test_basic()
    finally:
        test.quit()

if __name__ == "__main__":
    run_test()
