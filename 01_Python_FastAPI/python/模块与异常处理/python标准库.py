# 在安装python解释器后，这些标准库就可以直接使用，无需安装
# random模块：生成随机数
# random.randint(a,b) 生成一个从a到b（包含a,b）的随机整数
# random.choice(sequence):从一个序列中随机选择一个元素
import random

#生成一个从1到6的随机整除，模拟掷骰子
dice_roll=random.randint(1,6)
print(f"你掷出了{dice_roll}")
# 从列表中随机抽取一个幸运儿
participants=["李卓凡","呆跑","龙驹"]
luck_one=random.choice(participants)
print(f"恭喜{luck_one}中奖了！")

# datetime 模块：处理日期和时间
import datetime
now=datetime.datetime.now()
print(f"完整当前时间：{now}")

# 格式化输出
formatted_date=now.strftime("%Y-%m-%d %H:%M:%S")
print(f"格式化后的时间{formatted_date}")