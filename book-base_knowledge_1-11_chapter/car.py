class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        self.odometer_reading = 30
        # 通过__init__()增加一个形参里面没有的属性，并指定默认值是0.

    def get_descriptive_name(self):
        # describ  : 描述的意思
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self, miles):
        # incrment:让里程表增加的意思：
        self.odometer_reading += miles

    def full_gas_tank(self):
        self.fill_gas_tank = 0
        print(f"容量是{self.full_gas_tank}")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def upgrade_battery(self, battery_size=65):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"this car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

        self.battery = Battery()

    def full_gas_tank(self):
        print("This car has no gas tank.")
