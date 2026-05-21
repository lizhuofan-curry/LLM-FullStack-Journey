# 模块就是相当于c++里面的函数库或者是自己自定义的函数，从另外一个文件导入
# 为了确保不重复造轮子，和便于协作，在团队开发中使不同的人负责开发不同的模块
import math

print(f"圆周率PI约等于{math.pi:.20f}")

res=math.sqrt(25)
print(f"25的平方根为{res:.0f}")
# 导入模块的不同形式
# from import
# 只从math里面导入pi和sqrt
from math import pi,sqrt
print(f"圆周率PI为{pi}")
print(f"25的平方根为{sqrt(25)}")

# import ... as 给导入的模块起个别名
import datetime as dt
now=dt.datetime.now()
print(f"当前的时间为{now}")

# 还能取一个极简别名
from datetime import datetime as dt
print(dt.now())