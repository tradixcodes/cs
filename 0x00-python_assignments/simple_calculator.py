# SCT211-0009/2022
# Njoroge Kanyagia

name = input("Enter your name: ")

print(name +", choose the following options;")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

_operation = int(input("Choose 1-4:"))
print("Enter the two numbers")
num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

if _operation == 1:
    result = num1 + num2
elif _operation == 2:
    result = num1 - num2;
elif _operation == 3:
    result = num1 * num2
elif _operation == 4:
    if num2 == 0:
        print("Error: Division by zero")
        result = None
    else:
        result = num1 / num2
else:
    print("Invalid input")
    result = None
if result is not None:
    print("Result:", result)
