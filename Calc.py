#Python Calculator (Calc is short for calculator btw)

operator = input("Enter operator: (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2)) 
elif operator == "-":
    result = num1 - num2 
    print(round(result, 2)) 
elif operator == "*":
    result = num1 * num2
    print(round(result, 2)) 
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator, retard")