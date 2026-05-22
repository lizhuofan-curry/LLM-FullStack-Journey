from fastapi import FastAPI

# 1,实例化FastAPI 对象
app = FastAPI()


# 2.路径操作装饰器
# 含义：当客户端以 GET 方法访问根路径“/”时 运行下方函数
@app.get("/")
async def read_root() -> dict:
    # 3.路径操作函数
    # 直接返回字典 FastAPI会自动转换为JSON
    return {"message": "Hello World"}


# 新增/info 路由
@app.get("/info")
async def get_info() -> dict:
    return {
            "name": "fange",
            "role":"student",
            "language": "python 3.10"
    }

if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)
