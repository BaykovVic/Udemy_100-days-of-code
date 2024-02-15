def calculate(n, **kwargs):
    print(kwargs)
    print(kwargs["add"])
    #for key, value in kwargs:
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")

car = Car(make="Nissan", model="Skyline")
print(car.model)
