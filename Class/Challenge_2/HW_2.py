# HW - 1 - OOP - Challenge 2 - Time Class & Code Review

# the code that we write it in HW_1 
# class Time:
#     def __init__(self, hours, minutes, seconds):
#         self.hours, self.minutes, self.seconds = hours, minutes, seconds
#         self.normalize_time()
#         self.total_minute = self.hours * 60 + self.minutes
#         self.total_second = self.hours * 3600 + self.minutes * 60 + self.seconds

#     def normalize_time(self):
#         if self.seconds >= 60:
#             self.minutes += self.seconds // 60
#             self.seconds %= 60
#         if self.minutes >= 60:
#             self.hours += self.minutes // 60
#             self.minutes %= 60

#     def get_total_minutes(self):
#         return self.total_minute

#     def get_total_seconds(self):
#         return self.total_second

#     def set_time(self, hours, minutes, seconds):
#         self.hours, self.minutes, self.seconds = hours, minutes, seconds
#         self.normalize_time()
#         self.total_minute = self.hours * 60 + self.minutes
#         self.total_second = self.hours * 3600 + self.minutes * 60 + self.seconds

#     def __str__(self):
#         return f'Time is {self.hours:02}:{self.minutes:02}:{self.seconds:02}'


# if __name__ == '__main__':
#     time = Time(4, 112, 65)
#     print(time)
#     print("Total Minutes:", time.get_total_minutes())
#     print("Total Seconds:", time.get_total_seconds())
#     time.set_time(1, 70, 130)
#     print(time)




# The Optimized code
class TimeOptimized:
    def __init__(self, total_seconds):
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        total_seconds %= 60
        self.seconds = total_seconds

    def get_total_minutes(self):
        return self.minutes

    def get_total_seconds(self):
        return self.seconds

    def set_time(self, total_seconds):
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        total_seconds %= 60
        self.seconds = total_seconds

    def __str__(self):
        return f'Time is {self.hours:02}:{self.minutes:02}:{self.seconds:02}'


if __name__ == '__main__':
    time = TimeOptimized(65)
    print(time)
    print("Total Minutes:", time.get_total_minutes())
    print("Total Seconds:", time.get_total_seconds())
    time.set_time(5290)
    print(time)



