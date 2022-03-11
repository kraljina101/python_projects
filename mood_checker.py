mood = input("Kako se osjecas? ")

if mood == "sretno":
    print("Dobro je osjecati se " + mood + ".")
elif mood == "nervozan":
    print("Popij pivu pa neces biti " + mood + ".")
elif mood == "tuzan":
    print("Nemoj biti " + mood + ".")
elif mood == "uzbuđen":
    print("Ne valja biti previse " + mood + ".")
elif mood == "opušten":
    print("Lijepo je biti " + mood + ".")
else:
    print("Ne prepoznajem ovo raspoloženje !")
