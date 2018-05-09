# Credit Card Validator - Takes in a credit card number from a common credit card vendor (Visa, MasterCard,
# American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards
# use a checksum).
import re

while True:
    card_number = input("Enter your credit card number (Visa, MasterCard, American Express, Discoverer): ")
    pattern = '^(?:4[0-9]{12}(?:[0-9]{3})?|[25][1-7][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|' \
              '[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$'
    if not re.match(pattern, card_number):
        print("Wrong input!")
    else:
        print("Correct input!")
        break
