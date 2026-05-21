# Python里面的全局变量通常定义在文件顶部，一般为全大写
name="LIZHUOFAN"
def out():
    ## 如果我要修改的话，就用global 加变量名进行修改
    #global name
    name="李卓凡"
    print(f"{name}真帅")
if __name__=="__main__":
    out()
    print(f"现在全局变量变成了{name}")