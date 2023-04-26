# reading from external files such as pdf or CSV

employee_file = open("Dudes.txt", "r")            # r stands for read. only for reading what is in the file
                                             # w means you can wrtie on on the file
print(employee_file.readable())
print(employee_file.read()) # A means you can append means you can add
print(employee_file.readline())  # reads the first line and then moves the "cursor" down 1
print(employee_file.readlines())  # puts lines in the array----adding [1] is just goign to print positin 1 int he array
for employee in employee_file.readlines():  # loops through to print each line in the file
    print(employee)
employee_file.close()                           # r+ means reading and writing

# make sure to close the file




