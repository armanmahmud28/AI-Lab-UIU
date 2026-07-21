#Calculator Using Functions

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", add(a, b))
print("Subtraction =", sub(a, b))
print("Multiplication =", mul(a, b))
print("Division =", div(a, b))