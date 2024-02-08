"""
if 语句
"""


def cars_example():
    _cars = ['audi', 'bmw', 'subaru', 'toyota']
    for _car in _cars:
        if _car == 'bmw':
            print(_car.upper())
        else:
            print(_car.title())
    print("bmw" in _cars)
    print("audi" in _cars)
    print("audi" not in _cars)
    print("bmw" not in _cars)
    print("bmw" == "bmw")
    print("bmw" == "BMW")
    print("bmw".lower() == "BMW".lower())


def age_example(age: int):
    if age < 4:
        price = 0
    elif age < 18:
        price = 10
    elif age < 65:
        price = 5

    print("Your admission cost is $" + str(price) + ".")


if __name__ == '__main__':
    # cars_example()
    age_example(12)