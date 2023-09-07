from seleniumbase import BaseCase

class VisitGoormioPage(BaseCase):

    def test_visit_page(self):
        # 设置使用 Tor
        self.set_proxy_server("127.0.0.1:9050")
        
        # 访问网址
        self.open("https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13")
        # 停留一分钟
        self.sleep(60)

if __name__ == "__main__":
    case = VisitGoormioPage()
    case.test_visit_page()
