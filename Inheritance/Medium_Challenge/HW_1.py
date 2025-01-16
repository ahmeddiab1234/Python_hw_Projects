# HW - 1 - OOP - inhertance - Medium - Design Review

class FourWheels:
    #some variables and methods
    pass

class Engine:
    #some variables and methods
    pass

class Car(Engine, FourWheels):
    #some variables and methods
    pass


"""

Although this code will pass the system test but the design is wrong

why:
    Inheritance represents an "is-a" relationship. For example, if Car inherits from FourWheels, 
    it implies that a Car is a FourWheels, which is not logically accurate.
    Similarly, Car inheriting from Engine implies a Car is an Engine, which is also incorrect.
    The correct relationship here is "has-a": A Car has an Engine and has FourWheels. 
    This is best modeled using composition.

"""
