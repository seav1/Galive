import seleniumbase

class VisitGoormioPage(seleniumbase.BaseCase):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def set_proxy_server(self, proxy_url):
        proxy = webdriver.Proxy()
        proxy.proxy_url = proxy_url
        proxy.add_to_capabilities()
        self.driver.start_session(desired_capabilities=proxy.capabilities)

    def test_visit_page(self):
        self.set_proxy_server("127.0.0.1:9050")
        self.driver.get("https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13")
        self.sleep(60)

    def runTest(self):
        self.test_visit_page()

if __name__ == "__main__":
    case = VisitGoormioPage(driver=webdriver.Chrome())
    case.runTest()
