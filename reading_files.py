# modes can be a - append, r - read, w - write, r+ - read and write
employee_file = open("employees.txt", "r+")

# READ
print(employee_file.readable())
# print(employee_file.readline())

# only lines that were not read with 'readline' above will be read with
print(employee_file.read())

# 'readlines' stores the file content into a list
print(employee_file.readlines())  # add [2] to read a specific line

for employee in employee_file.readlines():
    print(employee)

# APPEND
employee_file.write("\nAlmir - Developer")

# CREATE NEW FILE
employee_file = open("employees2.txt", "w")
employee_file.write("Almir - Developer")

employee_file.close()
