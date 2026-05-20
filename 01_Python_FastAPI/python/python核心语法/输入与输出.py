#练习输出语句
name='lizhuofan'
age=18
print('大家好')
print("我的名字是",name)
print("我今年",age,"岁")
#python里面输出加,就够了，如果要在前面加入文字描述则用引号括住就行


#练习输入加输出语句
print("你好我是豆包，请问你叫什么名字")
name=input()
print("很高兴认识你",name,"!")

print("你今年多大了")
age=input()
print("原来你",age,"岁了")

# 注意看不管你输入的是什么类型的内容，你输出的都是字符串类型
# 这也是python的一个特性
print(type(name),type(age))