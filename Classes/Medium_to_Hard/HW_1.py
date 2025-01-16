# HW - 1 - Medium to Hard - Classes - MyRange Class

class MyRange:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
    def has_next(self):
        return self.start < self.end
    def get_next(self):
        prev = self.start
        self.start += self.step
        return prev

rng = MyRange(5, 10, 1)
while rng.has_next():
    print(rng.get_next(), end=' ') # 5 6 7 8 9
print()

rng = MyRange(5, 10, 2)
while rng.has_next():
    print(rng.get_next(), end=' ') # 5 7 9
