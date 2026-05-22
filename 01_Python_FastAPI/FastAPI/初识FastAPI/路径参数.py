# 路径参数是URL中的一部分，用来定位特定的资源
# 语法:
# 在装饰器路径中使用{variable_name}声明，并在函数参数中添加同名参数
# 类型转换：FastAPI会自动根据函数参数的类型提示进行转换

from fastapi import FastAPI
app=FastAPI()

# 路径参数item_id被定义为 int 类型
@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id,"type":str(type(item_id))}