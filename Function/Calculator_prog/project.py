def print_menu():
    while True:
        print("Menu:")
        print("Enter 1 to sum numbers from 1 to N")
        print("Enter 2 to evaluate simple 2 numbers expression (e.g. 2 + 3)")
        print("Enter 3 to end the program")
        choice = int(input("Enter a valid choice from 1 to 3: "))
        if choice in [1, 2, 3]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def divide(num1, num2, operation):
    if (operation == '/' or operation == '//') and num2 == 0:
        return None
    if operation == '/':
        return num1 / num2
    if operation == '//':
        return num1 // num2

def expression():
    ex1 = int(input("Enter the first number: "))
    op = input("Enter an operator (+, -, *, /, //, %, **): ")
    ex2 = int(input("Enter the second number: "))
    
    if op in ['/', '//']:
        result = divide(ex1, ex2, op)
        if result is None:
            print("Cannot divide by zero.")
            return
        else:
            print(result)
            return
    
    if op == '+':
        print(ex1 + ex2)
    elif op == '-':
        print(ex1 - ex2)
    elif op == '*':
        print(ex1 * ex2)
    elif op == '%':
        print(ex1 % ex2)
    elif op == '**':
        print(ex1 ** ex2)
    else:
        print("Invalid operator.")

def sum_1_to_n():
    N = int(input("Enter a number "))
    res = 0
    i = 1
    while i <= N:
        res += i
        i += 1
    print(f"Sum from 1 to {N} is {res}")


def calculator_interface():
    while True:
        choice = print_menu()
        if choice == 1:
            sum_1_to_n()
        elif choice == 2:
            expression()
        elif choice == 3:
            print("Exiting program.")
            break

calculator_interface()



