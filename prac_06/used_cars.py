"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Ferrari", 42, 177)
    my_car.drive(30)
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    limo.drive(115)

    print("{self.name}, fuel={self.fuel}, odometer={self.odometer}".format(self=my_car))
    print(limo.fuel)
    print(limo.odometer)
    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

main()
