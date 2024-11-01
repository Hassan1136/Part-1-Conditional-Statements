
# 13. Take two numbers and an operator (+, -, *, /) as input and perform the corresponding operation.

num1 = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
operator = input("Enter an operator (+,-,*,/): ")

if operator == "+" :
    print(num1, " + ", num2, " = ", num1 + num2)
elif operator == "-" :
    print(num1, " - ", num2, " = ", num1 - num2)
elif operator == "*" :
    print(num1, " * ", num2," = ", num1 * num2)
else:
    print(num2, " / ", num1, " = ", num1 / num2)