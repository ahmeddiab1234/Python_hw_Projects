# HW - 1 - Medium to Hard - Nested List - Implement our zip: v1


class OurZip:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.min_length = min(len(iterable) for iterable in iterables)
        self.index = 0

    def has_next(self):
        return self.index < self.min_length

    def get_next(self):
        if not self.has_next():
            raise StopIteration("No more elements to iterate.")
        result = tuple(iterable[self.index] for iterable in self.iterables)
        self.index += 1
        return result


if __name__ == '__main__':
    z = OurZip(list(range(10, 15)), list(range(100)), 'Mostafa')
    while z.has_next():
        print(z.get_next())


"""
(10, 0, 'M')
(11, 1, 'o')
(12, 2, 's')
(13, 3, 't')
(14, 4, 'a')
"""

