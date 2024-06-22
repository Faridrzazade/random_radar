import random

from random import randint

class Radar:
    def __init__(self, name, limit, max_speed):
        self.name = name
        self.limit = limit
        self.max_speed = max_speed
    
    def check_speed(self):
        random_speed = randint(0, 240)

        if self.limit <= random_speed <= self.max_speed:
            return "No fine"
        elif self.limit <= random_speed <= self.max_speed + 10:
            return "You were fined 10 manats"
        elif self.limit <= random_speed <= self.max_speed + 60:
            return "You were fined 50 manats and 2 points"
        elif self.limit <= random_speed <= self.max_speed + 120:
            return "You were fined 200 manats and 4 points"
        elif random_speed > self.max_speed + 120:
            return "You were fined 300 manats and 15 days in prison"
        else:
            return "The car moves below the speed limit"


    def belt(self):
        random_belt = random.choice(["belt_is_on", "not_wearing_a_belt"])
        if random_belt == "not_wearing_a_belt":
            return "You were fined 40 manats for not wearing a seat belt"
        elif random_belt == "belt_is_on":
            return "belt_is_on"



radar_road_1 = Radar("Road 1", 40, 49)
print(f"Road 1: {radar_road_1.belt()} \nRoad 1: {radar_road_1.check_speed()}\n" )

radar_road_2 = Radar("Road 2", 60, 69)
print(f"Road 2: {radar_road_2.belt()} \nRoad 2: {radar_road_2.check_speed()}\n")

radar_road_3 = Radar("Road 3", 90, 99)
print(f"Road 3: {radar_road_3.belt()} \nRoad 3: {radar_road_3.check_speed()}")

