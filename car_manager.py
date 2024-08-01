from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_y = random.randint(-250, 250)
            new_car.goto(320, new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed(self):
        self.car_speed += MOVE_INCREMENT









# def __init__(self):
#     super().__init__()
#     self.penup()
#     self.shape("square")
#     self.color(random.choice(COLORS))
#     self.shapesize(stretch_len=2)
#
# def create_cars(self):
#     new_y = random.randint(-250, 250)
#     self.goto(300, new_y)






