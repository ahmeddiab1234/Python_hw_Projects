# HW - 3 - More Functions - Reduce v2

def myreduce(func1_overall, func2_consecutive, iterable):
    try:
        a, b, *iterable = iterable
        result = func2_consecutive(a, b)
    except:
        return RuntimeError('The length of the sequence must be at least 2')

    while iterable:
        try:
            a, b, *iterable = iterable
        except:
            return RuntimeError('The length of the sequence must be even')
        result = func1_overall(result,func2_consecutive(a, b))

    return result


sum_lam = lambda x, y: int(x) + int(y)
multiply_lam = lambda x, y: int(x) * int(y)
max_lam = lambda x, y: x if x > y else y
min_lam = lambda x, y: x if x < y else y

print(myreduce(sum_lam, max_lam, [2, 5, 3, 4, 5, 10]))  
print(myreduce(multiply_lam, min_lam, [2, 5, 3, 4, 5, 10]))  
print(myreduce(sum_lam, min_lam, [2, 5, 3, 4, 5, 10]))  
print(myreduce(multiply_lam, max_lam, [2, 5, 3, 4, 5, 10]))
print(myreduce(multiply_lam, sum_lam, [2, 5, 3, 4, 5, 10]))