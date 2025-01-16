# HW - 2 - More Functions - Reduce v1

def myReduce(func, iterable, init=None):
    it = iter(iterable)
    if init is None:
        try:
            init = next(it)
        except StopIteration:
            raise TypeError("myReduce() of empty sequence with no initial value")
    for val in it:
        init = func(init, val)
    return init

sum_lam = lambda x, y: int(x) + int(y)
multiply_lam = lambda x, y: int(x) * int(y)
max_lam = lambda x, y: x if x > y else y
min_lam = lambda x, y: x if x < y else y

print(myReduce(sum_lam, [7, 20, 10]))  # 37
print(myReduce(multiply_lam, [7, 20, 10]))  # 1400
print(myReduce(max_lam, [7, 20, 10]))  # 20
print(myReduce(min_lam, [7, 20, 10]))  # 7
