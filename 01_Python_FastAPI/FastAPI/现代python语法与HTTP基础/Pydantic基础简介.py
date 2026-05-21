# FastAPI 使用Pydantic 库来定义数据类型 它强制执行类型提示，并在运行时进行数据验证
# 核心概念 通过继承 BaseModel 定义类
# 作用 如果数据不符合类型定义（例如需要int却传入了‘abc’ Pydantic会抛出友好的错误
from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    name : str
    price : float
    is_offer : bool =False # 默认为False

def test(name:str="world",price:float=1,is_offer:bool=False):
    return Item(name=name,price=price)
res=test()
print(res)