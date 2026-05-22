# 将路径参数和查询参数融合
# 获取某个特定商品分类下的商品列表，并且支持分页和搜索

from typing import Union
from fastapi import FastAPI

app=FastAPI()
# 路径参数和查询参数完美融合的接口
@app.get("/category/{category_name}/items")
async def get_category_items(
        category_name:str,   #1.路径参数: 确定是哪个分类（比如electronics，clothes)
        skip:int =0,         #2. 查询参数： 跳过多少条（默认0）
        limit:int =10,       #3. 查询参数： 限制返回多少条（默认10）
        q:Union[str,None] =None # 查询参数： 可选的搜索关键词（默认None)
):
    return {
        "message":f"正在查询【{category_name}】分类下的商品",
        "skip_count":skip,
        "limit_count":limit,
        "search_keyword":q,
        "status":"success"
    }

# 使能在PyCharm里面右键直接运行
# 同时增加规范性
if __name__ =="__main__":
    import uvicorn
    uvicorn.run("路径参数和查询参数融合:app",host="127.0.0.1",port=8000,reload=True)