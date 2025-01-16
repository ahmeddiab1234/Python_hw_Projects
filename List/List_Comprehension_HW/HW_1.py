# HW - 1 - Slicing and List Comprehension - Minimum of a type!

def find_smallest(lst, target_type):
    sum = [i  for i in lst  if type(i)==target_type]
    return min(sum) if sum else None

if __name__ == '__main__':
    lst = [10, -2.5, 20, 5, 'mostafa', 5.2, 'Ziad']
    print(find_smallest(lst,type(0))) # 5
    print(find_smallest(lst,type(0.0))) # -2.5
    print(find_smallest(lst,type(''))) # ziad

