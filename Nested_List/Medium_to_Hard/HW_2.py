# HW - 2 - Medium to Hard - Nested List - Implement our zip: v2


class OurZip:
    def __init__(self, *iterables):
        self.iterables = iterables
        self.max_length = max(len(iterable) for iterable in iterables)
        self.index = 0

    def has_next(self):
        return self.index < self.max_length

    def get_next(self):
        if not self.has_next():
            raise StopIteration("No more elements to iterate.")
        result = tuple(iterable[self.index] if self.index < len(iterable) else None for iterable in self.iterables)
        self.index += 1
        return result


if __name__ == '__main__':
    z = OurZip(list(range(10, 15)), list(range(10)), 'Mostafa')
    while z.has_next():
        print(z.get_next())


"""
(10, 0, 'M')
(11, 1, 'o')
(12, 2, 's')
(13, 3, 't')
(14, 4, 'a')
(None, 5, 'f')
(None, 6, 'a')
(None, 7, None)
(None, 8, None)
(None, 9, None)
"""

