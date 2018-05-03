# Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
number = input("What number do you want to find the Prime factors from? ")
number = int(float(number))
prime_factors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
my_prime_factors = []

while number != 1:
    for i in prime_factors:
        if number % i == 0:
            print(i)
            my_prime_factors.append(i)
            number = number / i
            break



print(my_prime_factors)