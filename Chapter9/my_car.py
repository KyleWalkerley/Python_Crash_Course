import battery
from car import Car as C
from electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'model s', 2019)
my_tesla.battery.describe_battery()
print(my_tesla.get_descriptive_name())
my_tesla.battery.get_range()


my_nissan = C('nissan','gtr','2020')
print(my_nissan.get_descriptive_name())