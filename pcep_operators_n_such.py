# ** makes an exponent

print(2**3)

print(2 ** 3)
print(2 ** 3.)   # if at least one argument is a float, the reult will be a float
print(2. ** 3)
print(2. ** 3.)


print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

# what if we want an integer?

# // is always divisional conforms to float rule and rounds

print(6 // 4)
print(6. // 4)  # rounding always goes to the lesser integer

print(-6 // 4)
print(6. // -4)

#  % is a remainder left after integer division; aka modulo

print(14 % 4)  # the answer here is 2 because 4 goes into 14 3 times... with *2* left over

print(12 % 4.5)


#  division by 0 does not work.

# addition

print(-4 + 4)
print(-4. + 8)

print(-4 - 4)
print(4. - 8)
print(-1.1)  # unary - operator

print(+2) # unary + operator

print(9 % 6 % 2)  # Binding to then left

print(2 ** 2 ** 3)  # exponential right side binding

print(2 * 3 % 5)

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

print((2 ** 4), (2 * 4.), (2 * 4))

print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

print((2 % -4), (2 % 4), (2 ** 3 ** 2))
