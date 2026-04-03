class Car:
    def __init__(self , brand , model):
        self.__brand = brand
        self.model = model

    def fuel_type(self):
        return "petrol or Diesel"

    def get_brand(self):
        return self.__brand + " !"

    def fullname(self):
        return f"{self.__brand} {self.model}"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand , model )
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"


s1 = Car("BMW", "DODGE")
my_tesla = ElectricCar("Tesla", "MOdel_S", "85kwh")


print(isinstance(my_tesla,Car))
print(isinstance(my_tesla, ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.get_brand())

