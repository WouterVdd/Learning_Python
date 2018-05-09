# Collatz Conjecture - Start with a number n > 1. Find the number of steps it takes to reach one using the
# following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

while True:
    try:
        number = int(float(input("Give in a number that's bigger than 1: ")))
    except:
        continue

    if type(number) is not int or number <= 1:
        continue
    else:
        counter = 0
        while number != 1:
            counter += 1
            if number % 2 == 0:
                number = number / 2
            else:
                number = number * 3 + 1
        print("It took %s steps to get to 1" % str(counter))
        break
