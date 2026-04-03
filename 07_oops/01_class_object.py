class Car:
    def __init__(self , userbrand , usermodel):
        self.brand = userbrand
        self.model = usermodel

s1 = Car("BMW", "DODGE")
s2 = Car("safari", "rolls royce")

print(s1.brand)
print(s1.model)

print(s2.brand)
print(s2.model)
    