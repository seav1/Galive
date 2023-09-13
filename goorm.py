from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_guest_visit(self):
        self.open("https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13")
        self.sleep(60)
