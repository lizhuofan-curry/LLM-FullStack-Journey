# 多态是指同一个方法的调用，在不同的对象上会产生不同的行为
# 它依赖于继承关系的实现，是OOP提高代码灵活性和可拓展的关键

# 简单理解：父类定义的方法，子类可以重写（覆盖），当通过子类调用该方法时
# 执行的是子类重写后的逻辑，而不是父类的逻辑

# 父类
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    # 父类定义的驱动方法
    def drive(self):
        print(f"{self.brand}以传统方式行驶（默认燃油驱动")
# 子类1 ElectricCar
class ElectricCar(Car):
    def __init__(self,brand,color,battery_size):
        super().__init__(brand,color)
        self.battery_size=battery_size
    # 重写父类的drive方法
    def drive(self):
        print(f"{self.brand}以电力驱动行驶，电池容量{self.battery_size}")

# 子类2 FuelCar
class FuelCar(Car):
    def __init__(self,brand,color,fuel):
        super().__init__(brand,color)
        self.fuel=fuel
    # 重写父类的drive方法
    def drive(self):
        print(f"{self.brand}以燃油驱动行驶，邮箱容量{self.fuel}")
# 多态的体现，同一个drive方法，不同对象执行不同逻辑
car1=ElectricCar("Tesla","Red",75)
car2=FuelCar("BMW","Black",60)
car3=Car("XYZ","Gray")
car1.drive()
car2.drive()
car3.drive()