# 语法格式
# 变量: 类型 =值
# def 函数名(参数 : 类型) -> 返回类型:

# 传统写法
def get_full_name(first_name,last_name):
    full_name=first_name+" "+last_name
    return full_name.title()
# 现代写法
def get_full_name1(first_name:str,last_name:str):
    full_name:str =first_name+" "+last_name
    return full_name.title()
##########

# 复杂类型（List,Dict,Optional,Union)
# List(列表） List[int] 表示一个只包含整数的列表
# Dict(字典） Dict[str,int] 表示键为字符串，值为整数的字典
# Optional(可选) Optional[str] 等同于 Union[str,none] ,表示该值可以是字符串，也可以是None
# Union(联合) Union[int,str]表示该值可以是整数或字符串
# 内置类型写法（List和Dict小写，这样子就不需要导入包）：
a: list[int] =[1,2,3]
b: dict[str,int]= {"age":18}
c: str|None=None
d: int|str =123

from typing import Optional,List,Dict,Union
# 定义一个处理分数的函数
def process_scores(scores:List[int]) -> Dict[str,float|int]:
    return {"average":sum(scores) / len(scores)}
# 定义一个允许缺省的搜索函数
def search_item(query:Optional[str])->Union[str,list[str]]:
    if query :
        return f"Searching for {query}"
    else : return ["item1","item2"]