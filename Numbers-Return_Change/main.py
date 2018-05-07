# Change Return Program - The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of €2, €1, 50, 20, 10, 5, 2, 1 cents needed for the change.
import logging

cost = 0
money_given = 0

while True:
    cost = round(float(input("How much is the cost? ")),2) * 100
    money_given = round(float(input("How much € is given? ")),2) * 100

    if cost > money_given:
        print("You haven't given enough money yet, try again.")
    elif cost == money_given:
        print("You don't need change it's paid perfectly.")
    else:
        break

owed = money_given - cost
amounts = [200, 100, 50, 20, 10, 5, 2, 1]
changes = {}
change = 0.0

while change != owed:
    for i in amounts:
        if i + change <= owed:
            if str(i)+"c" not in changes:
                changes[str(i) + "c"] = 1
            else:
                changes[str(i) + "c"] = changes[str(i) + "c"] + 1
            change += i
            break

print("You are owed %sc" % str(owed))
for item in changes.items():
        print(item)