from math import*  # introduces more math functions
print("hello world")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "Thomas"
character_age = 71

is_male = True
print("There was once an old man named " + character_name + ", ")
print("He was " + str(character_age) + " Years Old!")

character_name = "Miguelito"
print("He really liked the name " + character_name + ", ")
print("but he did not like being " + str(character_age))

phrase = "Giraffe Academy"
print("giraffe\" academy")

print(phrase)

print(phrase + " is cool")

print(phrase.lower())

print(phrase.upper())

print(phrase.isupper())

print(phrase.upper().isupper())

print(len(phrase))

print(phrase[0])

print(phrase.index("a"))

print(phrase.index("Academy"))

print(phrase.replace("Giraffe", "Elephant"))

print(-2.0987)

print((3 + 4.5) * 5) # specifying order of operation

print(10 % 3)   # TEN MOD 3  DIVIDED BY

my_num = 5

print(my_num)

print(str(my_num))

print(str(my_num) + " my favourite number")

my_num = -5

print(abs(my_num))

print(pow(3, 2)) # 3 to the power of 2 or 3 squared.

print(max(my_num, 4, 6))

print(min(my_num, 4, 6))

print(round(8.692))

print(floor(8.692))

print(ceil(8.692))

print(sqrt(8.692)) # square root

# getting input from users

words = input("put some stuff, like words or whatever- ")

other_words = input("put some other stuff, like words or whatever- ")

print("Yo diggity " + words + "!" + "How about " + other_words + "?")

num1 = input("Enter a number: ")

num2 = input("iOtra Vez!: ")

equals = num1 + num2 # default converted to string.

print(equals) # prints concatonated

num1 = input("Enter a number: ")

num2 = input("iOtra Vez!: ")

equals = int(num1 + num2) # converts to int

print(equals)

equals = int(num1) + int(num2) # converts to int

print(equals)

num1 = input("Enter a number: ")

num2 = input("iOtra Vez!: ")

equals = float(num1 + num2) # converts to int

print(equals)

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("roses are " + color )
print(plural_noun + " are blue")
print("i love " + celebrity)

# lists

friends = ["Michael", "John", "Joey"] # can put anything like strings numbers and booleans
#               0       1       2   indexes
print(friends)

print(friends[1]) # put the index number

print(friends[-1]) # pulls the index number from the back of the list

print(friends[1:3]) # Grabs up to the second number

friends[1] = "Mike" # Changing the index

print(friends[1])

# lists

fancy_number = [2, 3, 5, 7, 8]

fancy_friends = ["john", "michael", "joey", "erik", "liam"]

fancy_friends.extend(fancy_number)

print(fancy_friends) # appending the list

fancy_friends.append("MArio")

fancy_friends.insert(1, "Jenn") # adding a friened into the index

fancy_friends.remove("erik")

fancy_friends.clear()

fancy_friends.pop() # pops one off the top of the stack (last item)

print(fancy_friends.index("john"))

print(fancy_friends.index("erik"))

fancy_friends = ["john", "michael", "michael", "joey", "erik", "liam"]

print(fancy_friends.count("michael"))

fancy_friends.sort()

print(fancy_friends)

fancy_friends.reverse()

print(fancy_friends)

moar_friends = fancy_friends.copy # copies the list

# tuples- a container where we can store different values

coordinates = (4, 5) # () creates the tuple also, immutable, cannot be changes or modified.

print(coordinates[0]) # printing the index

# coordinates[1] = 10 - doesnt work because of immutability

# functions


def says_hi():            # def creates a function. all the code after the colon is for the function
    print("hello user") # must be indented
    print("please go away")


print("or not, I am not your mom") # 2 blank lines after function

says_hi()

print(fancy_friends)

fancy_friends = ["john", "michael", "michael", "joey", "erik", "liam"]


def says_hi_specifically(name):
    print("yo yo yu yo " + name)


says_hi_specifically("john")


def says_hi_moar_specifically(name, age):
    print("yo yo yu yo " + name + " u is " + age + "!")


says_hi_moar_specifically("john", 490)


def cube(num):                        # return statement returns information back from a function
    return num*num*num                # otherwise it will not return anything
# cannot put anything beyond a return statement


print(cube(6))

result = cube(5)

print(result)

# if statements

is_Male = True

is_tall = True


if is_male:   # must be true or false
    print("you are a male") # prints what is true will not print if false

else:
    print("you are not a male.")


if is_male or is_tall:  # must be true or false
    print("you are a male, tall or both")  # prints if one or both is true]

else:
    print("you are not a male nor are tall.") # both are false


if is_male and is_tall:  # must be true or false
    print("you are a male, tall or both")  # prints if one or both is true]

elif is_male and not is_tall:
    print("you are a short dude")

elif not is_male and is_tall:
    print("you are a tall lady")

else:
    print("you are not a male nor are tall.")  # both are false


# comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3: # either true or false (comparison operators) (== is the same as equals)
        return num1
    elif num2 >= num1 >= num3:   # != is not equals
        return num2
    else:
        return num3


print(max_num(3, 4, 5))


