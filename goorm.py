from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_guest_visit(self):
        self.open("https://ide-run.goorm.io/workspace/dGz54pALkYySfIqjBmp?token=ce166f5eccf285db2d818ed4c65a7c12&guestname=12")
        self.sleep(60)
