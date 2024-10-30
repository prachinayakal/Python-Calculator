# Python Calculator Program

This Python script implements a basic calculator that performs addition, subtraction, multiplication, and division based on user input.

## Features

- **Addition** (`+`)
- **Subtraction** (`-`)
- **Multiplication** (`*`)
- **Division** (`/`)

## How It Works

The `calculator()` function:
1. Prompts the user to choose an operation (`+`, `-`, `*`, or `/`).
2. Takes two numbers as input.
3. Performs the chosen operation.
4. Outputs the result.

If an invalid operation is entered, an error message is displayed.

## Example Usage

1. Run the program.
2. Choose an operation by typing one of the symbols: `+`, `-`, `*`, `/`.
3. Enter two numbers when prompted.
4. View the result of the calculation.

## Example Code

```python
def calculator():
    operation = input("Choose operation ( +, -, *, / ): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == '+':
        print("Result:", num1 + num2)
    elif operation == '-':
        print("Result:", num1 - num2)
    elif operation == '*':
        print("Result:", num1 * num2)
    elif operation == '/':
        print("Result:", num1 / num2)
    else:
        print("Invalid operation")

calculator()
