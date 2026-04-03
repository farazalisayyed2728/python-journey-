class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Battery:
     def battery_info(self):
         return "This is battery"


class Engine:
     def Engine_info(self):
         return "This is Engine info"


class ElectricCar_two(Car,Battery,Engine):
    pass

my_tesla_two = ElectricCar_two("Tesla", "MOdel_S")


print(my_tesla_two.battery_info())
print(my_tesla_two.Engine_info())
         
