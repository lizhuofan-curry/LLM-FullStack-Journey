# 修改字符串
# 将“abc”改为“bbc”
# 法一
s='abc'
res='b'+s[1:]
print(res)
# 法二
s=s.replace('a','b')
print(s)
#######
# 转义字符
# 1。\n 换行
# 2.\t 制表
# 3. \" 双引号
# 4. \\ 斜杠
print("你 \n好")
print("1 \n2")
print("a\tb")
print("he said \"hello\"")
print("c:\\Users\\python\\test.py")
# 前缀r取消转义
print(r"abc\ncc")