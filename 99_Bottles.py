# x bottles of beer on the wall, x bottles of beer.
# Take one down and pass it around, x-1 bottles of beer on the wall.

bottles = 99
# Declare bottles

while bottles >= 1:
    # Check if bottles is greater than or equal to 1
    newBottles = bottles-1
    # Make new variable where it is one less bottle
    if newBottles is 0:
        # If it's the final bottle
        print(f'{bottles} of beer on the wall, {bottles} of beer.\nTake one down and pass it around, no more bottles of beer on the wall.')
        # Then we have no more beer :c
        break
        # And we break out of the loop
    print(f'{bottles} of beer on the wall, {bottles} of beer.\nTake one down and pass it around, {newBottles} bottles of beer on the wall.\n')
    # If we still have beer, then say how much beer we have
    bottles = newBottles
    # Then we make bottles be newBottles for the next loop iteration
