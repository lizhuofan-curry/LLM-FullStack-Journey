# python里面的列表和c++不一样，里面可以存储不同类型的数据
# 比如我们创建一个包含不同数据类型的列表
# 注意我们通常使用[]来创建列表，而且可以随时增删改查，有先后顺序
my_list=["apple",100,3,14,True]
print(my_list)
for i in range(len(my_list)):
    print(my_list[i])
# 创建一个学生名单列表
students=["张三","李四","王五"]
print(students)
for j in students:
    print(j)
# python里面的-1是指最后一个位置
print(students[-1])
# 创建一个空列表
empty_list=[]
empty_list.append("第一个元素")
print(len(empty_list))
fruit_list=["apple","banana","orange","grape"]
# 直接遍历
for fruit in fruit_list:
    print(f"当前水果:{fruit}")
for index in range(len(fruit_list)):
     print(f"第{index}水果是{fruit_list[index]}")
# 增加元素：
# append(),在列表末尾添加一个元素
# insert() 在指定位置插入一个元素
# 删除元素：
# remove() 删除第一个匹配的元素
# pop() 删除并返回指定位置的元素（默认为最后一个）
# del 使用del关键字删除指定位置的元素
students.append("孙七")
print(students)
students.insert(0,"钱八")
print(students)
last=students.pop()
print(last)
print(students)
del students[0]
print(students)