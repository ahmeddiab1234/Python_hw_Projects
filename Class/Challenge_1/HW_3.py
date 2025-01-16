# HW - 2 - OOP - Classes - Datetime review 

class DateTime:
    def __init__(self, day, month, year, hours, minutes, second):
        self.day = day
        self.month = month
        self.year = year
        self.hours = hours
        self.minutes = minutes
        self.second = second


"""
Think in a critical design tip
○ Provide your feedback!
● Introduce a better design
"""

"""
- instead we send hours, day and year we can calculate them from we must do arithmetic operations to modify the code

- we must validate to ensure that the user will enter valid inputs to date 

- Leap Years: Every 4 years, February has 29 days. However, years divisible by 100 but not by 400 are not leap years.

"""
