# Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

while True:
    number = input("Until what number do you want the fibonacci sequence to be generated? ")
    number = int(float(number))
    if number < 100:
        list = []
        for i in range(0, number):
            if i <= 1:
                list.append(i)
            else:
                list.append(list[i-2] + list[i-1])
        print(list)
        break
    else:
        print("The sequence can only be generated on numbers under 100")