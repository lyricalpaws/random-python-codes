import sys

# Asks the user what to count to
y = input("What to count to?\n>")

ytest = str(y)

if ytest.isnumeric():
    y = int(y)  # Making y an integer to count to
else:
    sys.exit("That isn't a number!")

x = 1  # Setting x as 1, one is the starting number

print(x)  # Prints 1

# Loop that adds 1 to x and prints it
# Stops when x is the same number as y and prints the final number
while x is not y:
    x = x+1
    print(x)
