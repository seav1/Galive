from seleniumbase import BaseCase, config

class MyTestClass(BaseCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        config.set_headless_browser(False)  # 取消无头模式
        cls.driver = cls.open_browser()

    def test_basic(self):
        self.open('https://ide-run.goorm.io/workspace/dGz54pALkYySfIqjBmp?token=ce166f5eccf285db2d818ed4c65a7c12&guestname=12')
        time.sleep(60)  # 保持1分钟        

    def quit(self):
        self.driver.quit()

def run_test():
    test = MyTestClass()
    try:
        test.test_basic()
    finally:
        test.quit()

if __name__ == "__main__":
    run_test()
