# Importing modules for the program.
import random
import sys

# Setting the numbers that the generator can use when making the random number.
chars = '1234567890'

# Asks user how long each int string should be, and requires an input.
length = input("String length?\n> ")

# Checks if the inputted value is a number or not.
# If it is, set it as an integer. If not, return a message and end the process.
if length.isnumeric():
    length = int(length)
else:
    sys.exit("That isn't a number!")

# Same as before, but for number of strings rather than length.
amount = input("How many strings?\n> ")

# Also same as before with checks.
if amount.isnumeric():
    amount = int(amount)
else:
    sys.exit("That isn't a number!")


# If the user only wants one string it will say "Your string is",
# but if they wanted multiple strings then it will say "Your strings are:".
if amount > 1:
    print("Your strings are:")
else:
    print("Your string is:")

# Generates a string per the number of times said in the amount variable,
# then prints each string individually as a random string from the numbers variable.
for p in range(amount):
    numstring = ''
    for c in range(length):
        numstring += random.choice(chars)
    print(numstring)
