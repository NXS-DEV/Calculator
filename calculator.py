Greeting = "Welcome on the calculator\n"
Greeting1 = "Developed by: Noxious"
Version = 'The app version is : 0.0.0.5A'
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
        return x / y
    elif operation == "square":
        return x * x
    elif operation == "powers":
        return x ** y
    elif operation == "fraction":
        return "Coming soon"


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide, square, powers, fraction): ")

result = calculate(x, y, operation)
print("Result:", result)

# Next Update : Add factorial function [In progress]
# Next Update : Add a loop for made the program continue after one operation.
# Next Update : Add Graphical interface : Tkinter.
# Next Update : Divide the app in 2 section 1- basic function 2- advanced
