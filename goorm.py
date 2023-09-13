import requests
import time

url = 'https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13'

# 发送GET请求
response = requests.get(url)

# 等待1分钟
time.sleep(60)

# 输出响应内容
print(response.text)
