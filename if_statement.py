is_male = True
is_tall = False
gender = True
age = 33

if is_male and is_tall:
    result = "A person is a tall male"

elif is_male and (age > 18):
    result = "A person is a mature male"

elif not gender and not is_tall:
    result = "No gender"

else:
    result = "Not important"

print(result)


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3


largest_number = max_num(2, 3, 1)
print(largest_number)

