def add(*args):
    # return sum(args)
    sum = 0
    for i in args:
        sum += i
    return sum


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs['multiply']
    return n


class Car():
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')


print(add(1, 2, 3, 4, 5, 6, 7))
print(calculate(2, add=3, multiply=5))
car = Car(make='Nissan', model="GTR")
print(car.model)
car_2 = Car()
print(car_2.model)
