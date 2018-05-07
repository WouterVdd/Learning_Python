# Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or
# a binary number to its decimal equivalent.

choice = input("Do you want to convert a binary or decimal number? (b/d) ")
number = 0
converted = 0
if choice == "b":
    try:
        number = int(float(input("Give in a binary number: ")))
        converted = int(str(number), 2)
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")
        exit(-1)
elif choice == "d":
    try:
        number = int(float(input("Give in a decimal number: ")))
        converted = bin(number)
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")
        exit(-1)
else:
    print("Error: %s is not a valid choice!" % choice)
    exit(-1)

print("%s converted is: %s" % (str(number), str(converted)))