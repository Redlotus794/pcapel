class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year) -> None:
        self.make = make;  
        self.model = model;
        self.year = year;
        pass

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model;
        return long_name.title();
        pass;

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.");
        pass;


class ElectricCar(Car):
    def __init__(self, make, model, year) -> None:
        super().__init__(make, model, year)

if __name__ == '__main__':
    my_new_car = Car('audi', 'a4', 2016);
    print(my_new_car.get_descriptive_name());

    my_tesla = ElectricCar('tesla', 'model s', 2016);
    print(my_tesla.get_descriptive_name());
    pass;