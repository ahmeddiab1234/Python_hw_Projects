# HW - 1 - OOP - Challenge 2 - Time Class & Code Review


class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds

    def get_total_minutess(self):
        return self.hours * 60 + self.minutes
    
    def get_total_seconds(self):
        return self.hours * 60 * 60 + self.minutes * 60 + self.seconds
    
    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'



if __name__ == '__mian__':
    time = Time(2, 23, 14)
    print(time)

"""
1. Code Readability

The original code doesn't calculate total_minute and total_second in the constructor __init__, 
which results in repeated computation in get_total_minutess and get_total_seconds.
There's no method to allow the user to update the time after initialization, which makes the class less flexible.
"""

"""
2. Printing

The __str__ method isn't clear.
Simply printing the time in hh:mm:ss format might not make the ordered.
A more user-friendly output, such as "Time is hh:mm:ss", would improve clarity.
"""

"""
Can the user create a valid Timers and get unexpected answer?

yes if the user enter the time eg(Time(4, 112, 65))
in 112 minute it must be 1 hour and 52 minute 
in 65 hour it must be 1 minute and 5 second
"""


# New code

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.normalize_time()
        self.total_minute = self.hours * 60 + self.minutes
        self.total_second = self.hours * 3600 + self.minutes * 60 + self.seconds

    def normalize_time(self):
        if self.seconds >= 60:
            self.minutes += self.seconds // 60
            self.seconds %= 60
        if self.minutes >= 60:
            self.hours += self.minutes // 60
            self.minutes %= 60

    def get_total_minutes(self):
        return self.total_minute

    def get_total_seconds(self):
        return self.total_second

    def set_time(self, hours, minutes, seconds):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
        self.normalize_time()
        self.total_minute = self.hours * 60 + self.minutes
        self.total_second = self.hours * 3600 + self.minutes * 60 + self.seconds

    def __str__(self):
        return f'Time is {self.hours:02}:{self.minutes:02}:{self.seconds:02}'


if __name__ == '__main__':
    time = Time(4, 112, 65)
    print(time)
    print("Total Minutes:", time.get_total_minutes())
    print("Total Seconds:", time.get_total_seconds())
    time.set_time(1, 70, 130)
    print(time)