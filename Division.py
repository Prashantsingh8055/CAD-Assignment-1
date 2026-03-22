# Division Program

print("Division Program")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 != 0:
    result = num1 / num2
    print("The division of", num1, "by", num2, "is =", result)
else:
    print("Error: Division by zero is not allowed")