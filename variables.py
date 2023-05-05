#  ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#  the above characters have special meaning and should not be used as variable names

var = 1
print(var)

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

var = "3.8.5"
print("Python version: " + var)

var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

# Variables lab

john = 3

mary = 5

adam = 6

print(john, mary, adam)

print(john + mary + adam)


def total_apples(a, b, c):

    print(a + b + c)


total_apples(john, mary, adam)

all_apples = john + mary + adam

print(all_apples)
