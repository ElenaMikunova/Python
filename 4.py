import random


class Car:
    def __init__(self, a, b, c, d):
        self.name = a
        self.colour = b
        self.speed = c
        self.is_police = f"police? {bool(d)}."

    def go(self):
        print(f"Go {self.colour} {self.name}!")

    def stop(self):
        print(f"{self.colour.capitalize()} {self.name} stopped.\n")

    def turn(self):
        direction = random.choice(["right", "left", "back", "forward"])
        print(f"{self.colour.capitalize()} {self.name} goes {direction}!")

    def show_speed(self):
        print(f"{self.colour.capitalize()} {self.name} goes with speed {self.speed} km/h!")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.colour.capitalize()} {self.name} goes too fast to town car!")
        else:
            print(f"{self.colour.capitalize()} {self.name} goes with speed {self.speed} km/h!")


class PoliceCar(Car):
    def show_speed(self):
        print(f"{self.colour.capitalize()} {self.name} goes with speed {self.speed} km/h! "
              f"And it`s ok, it`s a police car and catching a criminal!")


class SportCar(Car):
    def show_speed(self):
        print(f"{self.colour.capitalize()} {self.name} goes with speed {self.speed} km/h! "
              f"And it`s ok, it`s a sport car!")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"{self.colour.capitalize()} {self.name} goes too fast to work car!")
        else:
            print(f"{self.colour.capitalize()} {self.name} goes with speed {self.speed} km/h!")


car_1 = SportCar("Hyundai", "blue", 120, 0)
car_1.go()
print(f"Is {car_1.colour} {car_1.name} with speed {car_1.speed} {car_1.is_police}")
car_1.turn()
car_1.show_speed()
car_1.stop()

car_2 = WorkCar("Lada Largus", "white", 45, 0)
car_2.go()
print(f"Is {car_2.colour} {car_2.name} with speed {car_2.speed} {car_2.is_police}")
car_2.turn()
car_2.show_speed()
car_2.stop()

car_3 = TownCar("Mazda", "red", 45, 0)
car_3.go()
print(f"Is {car_3.colour} {car_3.name} with speed {car_3.speed} {car_3.is_police}")
car_3.turn()
car_3.show_speed()
car_3.stop()

car_4 = PoliceCar("Chevrolet", "black", 150, 1)
car_4.go()
print(f"Is {car_4.colour} {car_4.name} with speed {car_4.speed} {car_4.is_police}")
car_4.turn()
car_4.show_speed()
car_4.stop()
