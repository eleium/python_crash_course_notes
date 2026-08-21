from car import ElectricCar,Car,Battery  # noqa: F401

my_new_car = Car("audi", "a4", "2024")
print(my_new_car.get_descriptive_name())


my_leaf = ElectricCar("nissan", "outback", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()