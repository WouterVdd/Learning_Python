# Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate.
# Also figure out how long it will take the user to pay back the loan.
# For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily).
import logging

base = float(input("What is the base price? "))
yearly_interest_rate = float(input("What's the interest rate? ")) / 100
interval = input("Is the interval Yearly, Monthly, Weekly, Daily? (y/m/w/d) ")

if interval.upper() == 'Y':
    interval = 1
elif interval.upper() == 'M':
    interval = 12
elif interval.upper() == 'W':
    interval = 52
elif interval.upper() == 'D':
    interval = 365
else:
    logging.error("Not a valid input!")
    exit(-1)


fixed_term = input("Is there a fixed term? (y/n) ")
if fixed_term.upper() == 'Y':
    terms = int(float(input("In how many terms do you need to pay this? ")))
    total = base * (1 + (yearly_interest_rate * (terms / interval)))
    print("You will need to pay %s in total" % round(total, 2))
    print("This will come down to monthly payments of %s" % round(total/terms,2))
elif fixed_term.upper() == 'N':
    base_capital = float(input("What's your starting capital? "))
    income = float(input("What is your yearly income? "))

    base -= base_capital
    base_capital = 0
    interest = 0
    i = 0
    while base > 0:
        base -= income / interval
        base += base * (1 + yearly_interest_rate / interval)
        i += 1
    print("You can pay off your debt in %s intervals " % i)


else:
    logging.error(fixed_term + " is not a valid input!")
    exit(-1)
