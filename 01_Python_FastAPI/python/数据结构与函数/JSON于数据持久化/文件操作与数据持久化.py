# 什么是数据持久化？
# 写文件：程序关闭前，将内存中的数据（如列表，字典）保存倒硬件上的文件中
# 读文件：程序启动时，从文件中读取数据，恢复倒文件中
# 打卡与关闭文件用with_open()语句
# 在实际开发中我们一般将python和json结合使用去存储列表，字典什么的
import json
# 序列化： 将python对象转化为json格式的字符串
# 操作有 1，json.dump(obj) 将JSON字符串转化为python对象
# 2， json.dump(obj,file) 将python对象转化为JSON格式并直接写入文件
# 反序列化： 将JSON格式字符串转化为python对象
# json.loads(str) :将json字符串转化成python对象
# json.load(file) :从文件中读取json数据并转化为python对象
#字典列表
contacts=[
    {'name':'Alice','phone':'111-2222','is_vip':True},
    {'name':'Bob','phone':'333-4444','is_vip':False}
]
# ------序列化：将数据写入文件---
file_path= "contacts.json"
with open(file_path,"w",encoding='UTF-8') as f:
    #使用json.dump() 直接读入文件
    json.dump(contacts,f)

# ------反序列化：从文件中读取数据------
with open(file_path,'r',encoding='utf-8') as f:
    load_contacts=json.load(f)

print("从文件中加载的数据：")
print(load_contacts)
print(f"加载第一个联系人状态：{load_contacts[0]['is_vip']}")

