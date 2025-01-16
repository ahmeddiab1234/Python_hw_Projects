# HW - 2 - Medium to Hard - Classes - MyRange Class (Flexible)

class MyRange:
    def __init__(self, start, end, step):
        if step > 0:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
        self.step = step
    def has_next(self):
        if self.step > 0:
            return self.start < self.end
        else:
            return self.start > self.end
    def get_next(self):
        prev = self.start
        self.start += self.step
        return prev
idx = 0
rng = MyRange(5, 10, 1)
while rng.has_next():
    print(f'({idx}, {rng.get_next()})') 
    idx +=1
print()

idx = 0
rng = MyRange(5, 10, 2)
while rng.has_next():
    print(f'({idx}, {rng.get_next()})') 
    idx +=1
print()

idx = 0
rng = MyRange(5, 10, -1)
while rng.has_next():
    print(f'({idx}, {rng.get_next()})') 
    idx +=1
"""
ex : 1
(0, 5)
(1, 6)
(2, 7)
(3, 8)
(4, 9)
"""
"""
ex : 2
(0, 5)
(1, 7)
(2, 9)
"""
"""
ex : 3
(0, 10)
(1, 9)
(2, 8)
(3, 7)
(4, 6)
"""

