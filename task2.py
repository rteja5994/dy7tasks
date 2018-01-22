import math

class Point():
    x = 0
    y = 0

class Rectangle():
    width = 0
    height = 0


    def __init__(self, initx, inity):
        self.width = initx
        self.height = inity
        self.corner = Point()

    def find_centre(self,corner):
        centre = ((corner.x+self.height)/2 , (corner.y+self.width)/2)
        return centre

p= Point()
p.x = 10
p.y = 20
r= Rectangle(100,200)

print(r.find_centre(p))