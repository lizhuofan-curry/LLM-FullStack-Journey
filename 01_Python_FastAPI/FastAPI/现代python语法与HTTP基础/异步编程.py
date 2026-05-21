# FastAPI 的高性能主要得益于对异步I/O的支持

# async 与 await 关键字
# async def 定义一个协程函数（Coroutine)
# await 挂起当前协程，等待耗时操作（如数据库查询，API调用）完成，期间释放CPU去处理其他请求
# 阻塞等待（time.sleep()) 非阻塞等待（asyncio.sleep())
import asyncio
import time

async def make_coffee():
    print("开始煮咖啡...")
    await asyncio.sleep(3) #煮咖啡需要三秒
    print("咖啡好了！")
async def make_toast():
    print("开始烤面包...")
    await asyncio.sleep(2) #烤面包需要两秒
    print("面包好了！")
async def main():
    start = time.time()

    await asyncio.gather(make_coffee(),make_toast())

    end =time.time()

    print(f"早餐做好了！总共花了{end-start:.2f}秒")
asyncio.run(main())

# async def 声明任务
# 用await asyncio.sleep() 优雅定闹钟
# 用asyncio.gather 让他们同时开工
# 用asyncio.run运行主函数