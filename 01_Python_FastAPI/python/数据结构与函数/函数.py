# python里面的函数定义只需使用def关键词
# 在调用时和c++一样，只不过更加智能，不用定义类型啥的，省去了很多繁琐的步骤
# 定义一个简单的问候函数
def greet():
    '''这是一个文档字符串，用于解释函数的功能'''
    print("hello,同学！,欢迎学习函数")

greet()
# 定义一个可以向特定的人问好的函数
def greet_person(name):
    print(f"hello,{name}很高兴认识你！")
name=input()
greet_person(name)

# 定义一个计算两数之和的函数
def add(num1,num2):
    res=num1+num2
    return res
# 注意这里的输入自动给你识别成字符串，所以你在在输入前加上类型
num1=int(input("请输入第一个数："))
num2=int(input("请输入第二个数："))
print(add(num1,num2))