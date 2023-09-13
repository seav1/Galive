# 获取当前时间
start_time=$(date +%s)

# 打开网址
xdg-open https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13

# 等待1分钟
sleep 60

# 获取当前时间
end_time=$(date +%s)

# 计算差值
duration=$((end_time - start_time))

# 打印差值
echo "网页保持打开状态${duration}秒"
