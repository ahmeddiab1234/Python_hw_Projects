# HW - 2 - OOP - inhertance - Medium - Future Prediction!


"""
The Mammal class is a parent class that defines methods such as givesMilk(), makeSound(), and givesLiveBirth().

The inhertance design is wrong as it suppose that all mammels are has givesMilk(), makeSound(), and givesLiveBirth() attripute but not all the mammels that give live birth 

Platypuses and echidnas are monotremes, meaning they lay eggs instead of giving live birth.

It tightly couples behaviors that are not universal to all mammals (e.g., live birth) with the base class.

to fix that Instead of assuming all mammals share certain behaviors, use composition to represent traits that are specific to certain mammals.

Separate behaviors like givesMilk, givesLiveBirth, and laysEggs into their own interfaces or classes.


"""

class Mammal:
    def givesMilk(self):
        return True

class LiveBirth:
    def givesLiveBirth(self):
        return True

class EggLaying:
    def laysEggs(self):
        return True

class Cat(Mammal, LiveBirth):
    def makeSound(self):
        return "Meow"

class Monkey(Mammal, LiveBirth):
    def makeSound(self):
        return "Ooh Ooh Ah Ah"

class Whale(Mammal, LiveBirth):
    def makeSound(self):
        return "Whale sound"

class Platypus(Mammal, EggLaying):
    def makeSound(self):
        return "Growl"
