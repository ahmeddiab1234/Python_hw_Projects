# HW - 1 - Classes - Medium - Rectangle and Circle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return (self.width * self.height ) 

class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def get_erea(self):
        return Circle.PI * self.radius * self.radius



r = Rectangle(2, 5)
print(r.get_area())  # 10

c = Circle(5)
print(c.get_erea()) # 87.5
