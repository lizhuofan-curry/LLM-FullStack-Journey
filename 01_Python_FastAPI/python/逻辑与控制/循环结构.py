# 循环

# for循环
# 通常配合range()函数使用for循环，range(n)可以生成0到n-1的整数序列
# 使用range()打印数字
print("counting from 0 to 4:")
for i in range(4):
    print(i)

# 遍历一个列表
fruits=["apple","banana","cherry"]
for fruits in fruits:
    print(fruits)

# 遍历一个字符串
for char in "python":
    print(char)
# while循环
# 语法
# while condition :
# # 当condition 为 True 时，重复执行里面的代码
# # 必须有代码的改变才能改变condition的状态

# 示例
countdown=4
while countdown>=0:
    print(f"conutdown:{countdown}")
    if countdown==2:
        break
    countdown=countdown-1
print("loop finished")
## 练习continue的用法
for j in range(1,20):
    if j%2==0:
        continue
    print(f"奇数{j}")