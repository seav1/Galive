from seleniumbase import BaseCase
from selenium.webdriver.common.proxy import Proxy, ProxyType

class VisitGoormioPage(BaseCase):

    def setup_class(self):
        # 设置使用 Tor
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': '127.0.0.1:9050',
            'sslProxy': '127.0.0.1:9050',
            'noProxy': ''
        })
        self.driver = self.get_new_driver(proxy=proxy)

    def test_visit_page(self):
        # 访问网址
        self.open("https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13")
        # 停留一分钟
        self.sleep(60)

if __name__ == "__main__":
    case = VisitGoormioPage()
    case.setup_class()
    case.test_visit_page()
