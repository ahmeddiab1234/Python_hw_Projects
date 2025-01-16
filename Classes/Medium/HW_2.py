# HW - 2 - Classes - Medium - Rectangle and Circle + Editor

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return  (self.width * self.height ) 

class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def get_erea(self):
        return  (Circle.PI * self.radius * self.radius)

class Editor:
    def __init__(self):
        self.r = None
        self.c = None

    def create_rectangle(self, width, height):
        self.r = Rectangle(width,height)

    def create_circle(self, radius):
        self.c = Circle(radius)

    def change(self, factor):
        if self.r == None:
            return
        self.create_rectangle(self.r.width+factor, self.r.height+factor)
        if self.c == None:
            return
        self.create_circle(self.c.radius + factor)

    def print(self):
        if self.r != None:
            print("Rectangle area " , self.r.get_area())
        if self.c != None:
            print("Circle area ", self.c.get_erea())

editor = Editor()
editor.create_rectangle(3,5)
editor.print() # Rectangle area 15
editor.create_circle(5)
editor.change(2)
editor.print() 
# Rectangle area 15
# Circle area 153.86

"""
r = Rectangle(2, 5)
print(r.get_area())  # 10

c = Circle(5)
print(c.get_erea()) # 87.5
"""