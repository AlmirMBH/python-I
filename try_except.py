try:
    number = int(input("Enter a number to divide with: "))
    result = 10 / int(number)
    print(result)
except ZeroDivisionError as err:
    print("Divided by zero. Python error: " + str(err))
except ValueError as err:
    print("Invalid input. Python error: " + str(err))

