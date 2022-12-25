from fractions import Fraction
Greeting = "Welcome on the calculator\n"
Greeting1 = "Developed by: Noxious"
Version = 'The app version is : 0.0.0.7'
print(Greeting + Greeting1)
print(Version)

def fraction(x):
    return Fraction(x).limit_denominator()

def calculate(x, y, operation):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        if y == 0:
            return "Error: Cannot divide by zero"
        return x / y
    elif operation == "square":
        return x * x
    elif operation == "square root":
        return x ** 0.5
    elif operation == "powers":
        return x ** y
    elif operation == "fraction":
        return fraction(x)
    else:
        return "Error: Invalid operation"

while True:
    try:
        x = float(input("Enter first number: "))
    except ValueError:
        print("Error! Invalid input for the first number")
        continue
    try:
        y = float(input("Enter second number: "))
    except ValueError:
        print("Error! Invalid input for the second number")
        continue
    operation = input("Enter operation (add, subtract, multiply, divide, square,square root, powers, fraction): ")
    result = calculate(x, y, operation)
    print("Result:", result)
