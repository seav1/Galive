from basecase import BaseCase

class VisitWebsite(BaseCase):

    def test_visit_goorm_io(self):
        self.open('https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13')
        self.sleep(60)  # Stay on the page for 60 seconds

if __name__ == "__main__":
    VisitWebsite().set_driver().run()
