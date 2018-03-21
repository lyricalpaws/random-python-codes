from random import randint

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))         # if Python 2.x use raw_input instead of input
        except ValueError:
            # not an int
            pass

def get_yn(prompt):
    while True:
        value = input(prompt).strip().lower() # if Python 2.x use raw_input instead of input
        if value in {'y', 'yes'}:
            return True
        elif value in {'n', 'no'}:
            return False

def roll(sides):
    return randint(1, sides)

def main():
    while True:
        sides = get_int("Number of sides on die (4, 6, or 12)? ")

        if sides in {4, 6, 12}:
            print("You rolled a {}".format(roll(sides)))
        else:
            print("U no reed gud?")

        if not get_yn("Play again (y/n)? "):
            print("Thanks for playing!")
            break

if __name__=="__main__":
    main()
