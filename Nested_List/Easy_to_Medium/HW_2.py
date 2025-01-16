# HW - 2 - Nested List - Easy to Medium - Triangular matrix

def trianlge_matrix():
    upper_sum,lower_sum = 0,0
    rows = int(input())
    list_of_list = [list(map(int, input().split())) for _ in range(rows)]
    for i in range(rows):
        for j in range(len(list_of_list[0])):
            if i >= j:
                lower_sum += list_of_list[i][j]
            if i <= j:
                upper_sum += list_of_list[i][j]
    return lower_sum, upper_sum

print(trianlge_matrix())


"""
3
8 16 9
3 15 27
14 25 29

94 (8+15+29+3+25+14)
104 (8+15+29+16+27+9)
"""
