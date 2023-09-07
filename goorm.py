from seleniumbase import BaseCase
from selenium.webdriver.common.proxy import Proxy, ProxyType

class VisitGoormioPage(BaseCase):

    def test_visit_page(self):
        # 设置使用 Tor
        PROXY = "127.0.0.1:9050"
        proxy = Proxy()
        proxy.proxy_type = ProxyType.MANUAL
        proxy.http_proxy = PROXY
        proxy.ssl_proxy = PROXY

        capabilities = self.options.to_capabilities()
        proxy.add_to_capabilities(capabilities)

        self.driver = self.create_driver(desired_capabilities=capabilities)

        # 访问网址
        self.open("https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13")
        # 停留一分钟
        self.sleep(60)

        self.driver.quit()

if __name__ == "__main__":
    case = VisitGoormioPage()
    case.test_visit_page()
