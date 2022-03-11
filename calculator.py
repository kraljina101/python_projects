broj_1 = int(input("Molimo vas unesite prvi broj: "))
broj_2 = int(input("Molimo vas unesite drugi broj: "))
operacija = input(
    "Molimo vas unesite koju racunsku operaciju zelite (+, -, *, /): ")


if operacija == "+":
    zbroj = broj_1 + broj_2
    print("Zbroj brojeva koje ste odabrali jest " + str(zbroj) + ".")
elif operacija == "-":
    razlika = broj_1 - broj_2
    print("Razlika dvaju unesenih brojeva jest " + str(razlika) + ".")
elif operacija == "*":
    umnozak = broj_1 * broj_2
    print("Umnozak dvaju unesenih brojeva jest " + str(umnozak) + ".")
elif operacija == "/":
    produkt = broj_1 / broj_2
    print("Produkt dvaju unesenih brojeva jest " + str(produkt) + ".")
else:
    print("Wrong input, please try again.")
