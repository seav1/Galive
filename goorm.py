class VisitGoormioPage(BaseCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.set_proxy_server("127.0.0.1:9050")

    def test_visit_page(self):
        self.driver.get("https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13")
        self.sleep(60)

if __name__ == "__main__":
    case = VisitGoormioPage(driver=webdriver.Chrome())
    case.test_visit_page()
