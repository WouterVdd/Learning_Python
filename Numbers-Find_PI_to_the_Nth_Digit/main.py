# Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
# Keep a limit to how far the program will go.
from math import pi


while True:
    number = input("Until what digit do you want to know PI? ")
    number = int(float(number))
    if number < 100:
        result = format(pi,  '.' + str(number) + 'f')
        print(result)
        break
    else:
        print("Try a smaller number of digits")
