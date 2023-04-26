# try/except
try:
    value = 10/0
    number = int(input("Enter a number"))
    print(number)
except ZeroDivisionError as err:   # err will print the error message
    print(err)

except ValueError:
    print("Invlaid input")

# always use specific errors

