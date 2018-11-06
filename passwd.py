# Importing modules for the program.
import random
import sys

# Setting the characters that the generator can use when making passwords.
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-!?$'

# Asks user how long each password should be, and requires an input.
length = input("Password length?\n> ")

# Checks if the inputted value is a number or not.
# If it is, set it as an integer. If not, return a message and end the process.
if length.isnumeric():
    length = int(length)
else:
    sys.exit("That isn't a valid number!")

# Same as before, but for number of passwords rather than length.
amount = input("How many passwords?\n> ")

# Also same as before with checks.
if amount.isnumeric():
    amount = int(amount)
else:
    sys.exit("That isn't a valid number!")


# If the user only wants one password it will say "Your password is",
# but if they wanted multiple passwords then it will say "Your passwords are:".
if amount > 1:
    print("Your passwords are:")
else:
    print("Your password is:")

# Generates a password per the number of times said in the amount variable,
# then prints each password individually as a random string from the chars variable.
for p in range(amount):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
