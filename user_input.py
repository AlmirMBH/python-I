
# name = input("Enter your name: ")
# last_name = input("Enter your last name: ")
#
# print("Hello, " + name + " " + last_name + "!")

# calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    result = num1+num2

elif operator == "-":
    result = num1-num2

elif operator == "*":
    result = num1*num2

elif operator == "/" and (num2 != 0):
    result = num1 / num2

elif operator == "/" and (num2 == 0):
    result = "Division with 0 not allowed"

else:
    result = "Invalid operator or numbers"


print(result)
