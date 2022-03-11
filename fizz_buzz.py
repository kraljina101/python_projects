number = int(input("Please enter a number from 1 to 100: "))

for x in range(1, number+1):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
    if x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
