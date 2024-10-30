def calculator():
    operation = input("Choose operation ( +, -, *, / ): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == '+':
        print("Result:",num1+num2)
    elif operation == '-':
        print("Result:",num1-num2)
    elif operation == '*':
        print("Result:",num1*num2)
    elif operation == '/':
        print("Result:",num1/num2)
    else:
        print("Invalid operation")
calculator()