number = int(input("how many numbers do you like?"))
numbers =[]

for x in range(number):
    ask = input ("numbers?:")
    numbers.append(ask)

    print("number")

for number in numbers:
    if number > 0:
       print(number + "positive")
    elif number < 0:
        print(number + "negative")
    else:
        print("error")
