# 查询参数声明在函数参数中，但不在路径{}中的参数，会被自动解释为查询参数
# 即URL中？后面的部分
# 默认值： 给参数赋值即可设置默认值
# 可选参数： 将类型设置为Optional[str] =None
# 布尔值转换 客户端传Yes,on,1,true 都会被自动转换为Python的true
from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/")
async def read_users(
        skip: int = 0,
        limit: int = 10,
        q: Union[str, None] = None
):
# URL 示例：/users/?skip=20&limit=5&q=admin
    return{"skip":skip,"limit":limit,"q":q}