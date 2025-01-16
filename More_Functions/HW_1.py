# HW - 1 - More Functions - Filter

def myfilter(func, iterable):
    res = [ val for val in iterable if func(val)]
    return res


is_even = lambda x: x%2 ==0
res = myfilter(is_even, [1, 2, 3, 4, 5, 6, 10, 13])
print(res) # [2, 4, 6, 10]

