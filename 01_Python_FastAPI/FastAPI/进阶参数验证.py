# FastAPI 提供了 Query Path Body 等类，配合Pydantic 的 Field 可以进行及其细致的数据校验
# Path/Query 校验：限制长度，正则表达式
# Field 校验 ：用于Pydantic模型内部，限制数值范围等
from fastapi import Query,Path,Body,FastAPI
from pydantic import BaseModel,Field

app=FastAPI()

class Calculator(BaseModel):
    #Field 用于模型内部校验：必须大于0，且小于10000
    num_a:float =Field(...,gt=0,lt=10000,description="第一个数字")
    num_b:float=Field(...,description="第二个数字")

@app.get("/items/{item_id}")
async def read_items(
        # Path 用于路径参数校验：必须大于等于1
        item_id:int =Path(...,ge=1,title="The ID of the item"),
        # Query 用于查询参数校验：限制最大长度为50
        q :str|None =Query(None,max_length=50)
):
    return {"item_id":item_id,"q":q}

# 一些参数的解释
# gt :greater than 大于
# lt :less than 小于
# ge : greater than or equal (大于等于)
# ... (Ellipsis):代表该字段是必填的，没有默认值