class Car:
    total_car = 0
    def __init__(self , brand , model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def fullname(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "petrol or Diesel"
    
    @staticmethod 
    def general_describtion():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand , model )
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


Car("BMW", "DODGE")
my_car = Car("Tata", "Safari")
# my_car.model = "City"
Car("Tata", "Nexon")

# print(my_car.general_describtion())

# print(Car.general_describtion())
print(my_car.model )