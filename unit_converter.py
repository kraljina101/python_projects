print("Greetings user, welcome to Smart Unit Converter.")

while True:
    kilometri = int(input("Please enter a number of kilometers: "))
    milje = kilometri * 0.62
    print(f"Your requsted answer is {milje} miles.")
    print("")

    kilometri_2 = input("Would you like to take another conversion? (yes/no) ")
    kilometri_lower = kilometri_2.lower()

    if kilometri_lower == "no":
        print("Thank you for your response, goodbye!")
        break
