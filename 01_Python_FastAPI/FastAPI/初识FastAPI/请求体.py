# 对于复杂的POST/PUT请求，我们需要定义数据结构
# Pydantic 是FastAPI的基石，用于数据验证和设置管理
# 定义Pydantic模型（BaseModel）
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app=FastAPI()

# 1.定义数据类型
class Item(BaseModel):
    name:str
    price:float
    is_offer:bool =None # 可选字段，默认为None
    description:Optional[str]=None # 将模型作为类型提示用于参数
    tax :Optional[float]=None
    price_with_tax:Optional[float]=None

@app.post("/item/")
async def creat_item(item:Item): #item此时已是Item类的实例，拥有属性提示
    item_dict=item.model_dump()
    if item.tax :
        price_with_tax=item.price+item.tax
        item_dict.update({"price":price_with_tax})

