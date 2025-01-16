# HW - 5 - More Function - Nested Lambda

sq = lambda a: a*a

def ff1(st, en, step):
    def clusher(f):
        return [f(val) for val in range(st, en, step) ]
    return clusher
processor1 = ff1(2, 6, 1)
print(processor1(sq)) # [4, 9, 16, 25]

# -------------------------------- #

ff2 = lambda st,en,step: lambda f: [f(val) for val in range(st, en, step)]

processor2 = ff2(2, 6, 1)
print(processor2(sq)) # [4, 9, 16, 25]
