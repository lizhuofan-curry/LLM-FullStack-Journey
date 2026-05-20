
# 定义一个存储学生成绩的字典
# 一般是用花括号来创建字典
# 其中key为名字，value为成绩
student_list= {
    "zhuofan":100,
    "daipao":60,
    "longju":70
}
print(student_list)
# 访问元素：通过key来访问对应的value
print(student_list["zhuofan"])
print(student_list["daipao"])
# 这样访问其实并不安全，如果不存在的话它不会像c++那样帮你自动创建
# 所以一般选择更安全的方式，使用.get()方法，如果key不存在，就不会报错
print(student_list.get("zhuofa"))
# 遍历所有key
for name in student_list:
    print(f"{name} is {student_list[name]}")
for name in student_list.keys():
    print(f"学生姓名：{name},成绩：{student_list[name]}")
# 遍历value
for score in student_list.values():
    print(f"学生成绩:{score}")
for name,score in student_list.items():
    print(f"学生姓名：{name},学生成绩为：{score}")
# 常用操作： 增加，修改，删除
student_list["shab"]=50
print(student_list)
del student_list["shab"]
print(student_list)