# HW - 3 - OOP - inhertance - Medium - Irrelevant!


class Robot:
    def drive(self):
        pass
    def clean(self):
        pass
    def do_funny_actions(self):
        pass

class RealAnimal:
    def go_toelit(self):
        pass
    def make_sound(self):
        pass
    def do_funny_actions(self):
        raise NotImplemented
    
class Cat(RealAnimal):
    def make_sound(self):
        print('Meow')
    
class Dog(RealAnimal):
    def make_sound(self):
        print('Bark')


"""

if we want to create class that has a relationship of "is a" with the 4 classes
there is some issues will force us as
there is no parent class that can have the all relationship of this four classes
the cat and dog is animals but robot is anothe type its machine 
and real animal is a generic class of animals

we can use the composition instead that it has the relationship "has a " 

"""

"""

if we want to make RobotDog class that has both the functionalities of robot class and dog class
we can design it with multiple inhertance

class RobotDog(Robot, Dog):
    def __init__(self):
        Robot.__init__(self)
        Dog.__init__(self)

robot_dog = RobotDog()
robot_dog.drive()
robot_dog.make_sound()

we can also used composition to avoid the problems of multiple inhertance    

"""