class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

model_x = Vehicle(200, 18000)
print(model_x.max_speed)
print(model_x.mileage)

print()

bmw = Vehicle(240, 18)
audi = Vehicle(123, 43)
print(bmw.__dict__)
print(audi.__dict__)