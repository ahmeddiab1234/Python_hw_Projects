# HW - 5 - Medium to Hard - Nested List - Active Robot

def ropot():
    inputs = input().split()
    row, col = int(inputs[0]), int(inputs[1])
    commands = inputs[2:]
    i, j = 0, 0
    
    for k in range(0, len(commands), 2):
        direction = commands[k].lower()
        steps = int(commands[k + 1])
        
        if direction == "right":
            j = (j + steps) % col
        elif direction == "left":
            j = (j - steps) % col
        elif direction == "up":
            i = (i - steps) % row
        elif direction == "down":
            i = (i + steps) % row
        
        print(f"({i}, {j})", end=" ")

ropot()



"""
3 4 right 1 down 2 left 2 up 3
(0, 1) (2,1) (2, 3) (2, 3)
"""
