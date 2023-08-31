from selenium import webdriver
from pyvirtualdisplay import Display
import time

display = Display(visible=0, size=(800, 600))
display.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=options)
driver.get("https://ide-run.goorm.io/workspace/d9Sssb0cUEnisCoRCgX?token=d04702b4519674ab9a512f72b1bae53d&guestname=12")

# 保持打开状态1分钟
time.sleep(60)

driver.quit()
display.stop()
