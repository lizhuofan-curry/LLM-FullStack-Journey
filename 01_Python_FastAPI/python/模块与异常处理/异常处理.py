# 异常是指程序在运行期间发生的错误,遇到无法处理的问题时，抛出一个异常
# ValueError 尝试将无法转换为数字的字符串（如‘hello’传递给int()函数）
# ZeroDivisionError:尝试用一个数除以0
# FileNotFoundError :尝试打开一个不存在的文件

# 这段代码会引发ValueError 并导致程序崩溃
# user_input=input("请输入一个数字")
# number=int(user_input)
# print(f"你输入的数字是{number}")

# 为了捕获并处理异常，我们通常使用try except语句块
for i in range(10):
    try:
        user_input = input("请输入一个数字")
        number = int(user_input)
        print(f"你输入的数字是{number}")
    except:
        print("错误！ 请输入有效数字，而不是文本")
        print("程序继续执行...")
        continue
