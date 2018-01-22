import math

class Point():
    x = 0
    y = 0

class Rectangle():
    width = 0
    height = 0
    corner = Point()

    def __init__(self, initx, inity):
        self.width = initx
        self.height = inity
        self.corner = Point()

    def find_centre(self,corner):
        centre = ((corner.x+self.height)/2 , (corner.y+self.width)/2)
        return centre

    def move_rectangle(self,dx, dy):
        ect = ((self.corner.x + dx), (self.corner.y + dy))
        return ect

p= Point()
p.x = 10
p.y = 20
r= Rectangle(100,200)
r.corner = p

print(r.find_centre(p))
print(r.move_rectangle(5,5))