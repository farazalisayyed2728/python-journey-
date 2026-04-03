class Car:
    def __init__(self , userbrand , usermodel):
        self.brand = userbrand
        self.model = usermodel

    def fullname(self):
        return f"{self.brand} {self.model}"
    
s1 = Car("BMW", "DODGE")


print(s1.brand)
print(s1.model)
print(s1.fullname())
