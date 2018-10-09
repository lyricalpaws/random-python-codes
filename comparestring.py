# Importing sys, don't need any other packages
import sys

# Asks for the first string to compare
print("\n")
string1 = input("First string to compare: ")
string1 = str(string1)

# Asks for the second string to compare
print("\n")
string2 = input("Second string to compare: ")
string2 = str(string2)

# Compares the two strings against eachother
# If they are the same, it returns "Both strings are the same"
if string1 == string2:
    print("\n")
    sys.exit("Both strings are the same")
else:
    print("\n")
    sys.exit("Both strings are different")
# If not, it returns "Both strings are different"
