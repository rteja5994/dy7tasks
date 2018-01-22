import math


class Point():
    x = 0
    y = 0

    def __init__(self, initx, inity):
        self.x = initx
        self.y = inity

    def distance_between_points(self):
        dist = math.sqrt((self.x ** 2) + (self.y ** 2))
        return dist

p = Point(5,9)
print(p.distance_between_points())
