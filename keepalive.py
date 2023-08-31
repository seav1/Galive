import time
from selenium import webdriver

# 指定要访问的网址
url = "https://ide-run.goorm.io/workspace/d9Sssb0cUEnisCoRCgX?token=d04702b4519674ab9a512f72b1bae53d&guestname=12"

# 启动一个 Chrome 浏览器
driver = webdriver.Chrome()

# 访问网址
driver.get(url)

# 等待 1 分钟
time.sleep(60)

# 关闭浏览器
driver.close()
