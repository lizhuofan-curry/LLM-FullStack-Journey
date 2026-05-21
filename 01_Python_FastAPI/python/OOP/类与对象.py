# 类定义了一类事物共有的属性和方法
# 在python中我们使用class关键词来定义一个类
# 定义一个最简单的“汽车”类
# 新定义一个方法
class Car:
    # pass # pass 是一个占位符，表示什么都不做
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        self.is_running=False
        #定义一个启动方法
    def start_engine(self):
        if not self.is_running:
            self.is_running=True
            print(f"{self.brand}的引擎启动了！")
        else :
            print("引擎已经在运行了。")
# 对象是根据类这个蓝图创造出的具体实例
# 在python中，我们调用类名来创建一个对象，这个过程称为实例化

# 根据Car 类的蓝图，创建两个具体的汽车对象
my_tesla=Car("Tesla","蓝色")
your_bmw=Car("BMW","红色")
# 我们用点.来访问一个对象属性，和c++里面访问结构体差不多
print(f"我的车是{my_tesla.brand},它的颜色是{my_tesla.color}")
print(f"你的车是{your_bmw.brand},它的颜色是{your_bmw.color}")
# 这里要用.来调用我们刚刚定义的函数
my_tesla.start_engine()
my_tesla.start_engine()
your_bmw.start_engine()
