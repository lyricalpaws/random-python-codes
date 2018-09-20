import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

length = input("Password length? ")
length = int(length)

amount = input("How many? ")
amount = int(amount)

for p in range(amount):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print("Your password is: " + password)
