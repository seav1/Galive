#!/bin/bash

# 获取当前时间
now=$(date +"%H:%M:%S")

# 每小时访问一次网址
while true; do
    # 检查当前时间是否为整点
    if [[ "$now" =~ ^[0-9]?:[0-9]?:[00]$ ]]; then
        # 访问网址
        open https://ide-run.goorm.io/workspace/dO8D4ys44ocxrovRqIA?token=0312731cf35a27ab2f073e3553c775dc&guestname=13
        # 保持打开状态 1 分钟
        sleep 60
    fi
    # 获取下一个整点时间
    next_hour=$(date -d "$now + 1 hour" +"%H:%M:%S")
    # 等待下一个整点
    until [[ "$now" = "$next_hour" ]]; do
        now=$(date +"%H:%M:%S")
        sleep 1
    done
done
