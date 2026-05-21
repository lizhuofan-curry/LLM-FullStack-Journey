# 继承是一种创建新类的机制，新类（称为子类或者派生类）
# 可以继承一个已经存在的类（称为父类或基类）的属性和方法
# 它的好处有可以代码复用，建立层级关系
# 父类
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def drive(self):
        print(f"{self.brand}正在路上行驶...")

# 子类 电车
class ElectricCar(Car):
    def __init__(self,brand,color,battery_size):
        super().__init__(brand,color)
        self.battery_size=battery_size

    # 子类的新方法
    def charge(self):
        print(f"正在为{self.brand}充电，电池余量{self.battery_size}")

# 创建子类对象
my_car=ElectricCar("Nissan Leaf","red",40)
# 调用继承父类的方法
my_car.drive()
# 调用子类的新方法
my_car.charge()