Greeting = "Welcome on the calculator\n"
Greeting1 = "Developed by: Noxious"
Version = 'The app version is : 0.0.0.6'
print(Greeting + Greeting1)
print(Version)


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
    elif operation == "powers":
        return x ** y
    elif operation == "fraction":
        return "Coming soon"
    else:
        return "Error: Invalid operation"

while True:
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        operation = input("Enter operation (add, subtract, multiply, divide, square, powers, fraction): ")
        result = calculate(x, y, operation)
        print("Result:", result)
    except ValueError:
        print("Error: Invalid input")
