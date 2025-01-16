# HW - 1 - Medium - Function - Print def special multiplication

def special_multiplication(string):
    for idx, rep in enumerate(string, start=1):
        for i in range(idx):
            print(rep, end='')
        

special_multiplication("abcxf")
