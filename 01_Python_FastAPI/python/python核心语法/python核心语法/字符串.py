# 在python中字符串的用法比较灵活
# 可以用''单引号 " "双引号 ''' '''三引号包裹
# 其中三个引号可以实现多行输出
str1='lizhuofan'
str2="handsome"
str3='''li
zhuo
fan
zhen
shuai'''
print(str1)
print(str2)
print(str3)

#############
# 字符串访问
s='abcdefg'
print(s[1])
print(s[0:3])
print(s[::1])
# 这在python中是实现字符串反转的小技巧
print(s[::-1])

###############
# 字符串常用操作
# 1.拼接与重复
a="lizhuofan"
b="zhenshuai"
print(a+" "+b)
# a.upper(),a.lower()分别表示变为大小写
print(a.upper())
# "a,b,c".split()表示分割成列表
print(a.split())
# "abc".replace("a","x") 将字符串里面的a变成字母x
print(a.replace("a","b"))
# a.count("x")
## 一种修改字符串的好方法
a=a.replace("a","b")
print(a.count("b"))
###########
# 格式化字符串
print(f"{a}{b}")
print(f'''我的名字叫{a}s
你可以对我说{b}''')
d=10.66
e=1.02
print(f"d+e={d+e:.3f} d*e={d*e:.3f}")