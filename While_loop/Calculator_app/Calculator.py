# HW - Medium - While Loop - Special Calculator

num = 1

while num <= 3:
    print("Enter 1 to sum numbers from 1 to N")
    print("Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)")
    print("Enter 3 to end the program")
    print("\nEnter choice from 1 to 3")
    val = int(input())
    
    if val == 1:
        N = int(input("Enter a number "))
        N-=1
        res = 0
        i = 1
        while i <= N:
            res += i
            i += 1
        print(f"Sum from 1 to {N+1} is {res}")
        
    elif val == 2:
        ex1 = int(input("Enter the first number: "))
        op = input("Enter the operator (+, -, *, /, //, %, **): ")
        ex2 = int(input("Enter the second number: "))
        
        if op == '+':
            print(ex1 + ex2)
        elif op == '-':
            print(ex1 - ex2)
        elif op == '*':
            print(ex1 * ex2)
        elif op == '/':
            print(ex1 / ex2)  
        elif op == '//':
            print(ex1 // ex2)  
        elif op == '%':
            print(ex1 % ex2)  
        elif op == '**':
            print(ex1 ** ex2)  
        else:
            print("Invalid operator.")
            
    elif val == 3:
        print("Program ended.")
        break
        
    else:
        print("Invalid Input...Try again")



