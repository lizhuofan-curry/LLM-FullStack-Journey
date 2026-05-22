# 任务描述 ： 创建一个API,支持加减乘除运算
# 要求：
# 1.使用POST 请求接收数据
# 2.使用Pydantic模型定义输入（包含操作数a,b和运算符 op）
# 3.对除数不能为0进行逻辑校验

from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Operation(str,Enum):
    add="+"
    subtract="-"
    multiply="*"
    divide="/"

class CalcRequest(BaseModel):
    a:float
    b:float
    op:Operation

# 使用枚举限制运算符
@app.post("/calculate")
async def calculate(request: CalcRequest):
    if request.op == Operation.divide and request.b==0:
        return {"error":"初始不能为0"}
    result=0
    if (request.op == Operation.add):
        result=request.a+request.b
    elif request.op == Operation.subtract:
        result =request.a -request.b
    elif request.op == Operation.multiply:
        result=request.a * request.b
    elif request.op == Operation.divide:
        result = request.a / request.b

    return{"result":result}