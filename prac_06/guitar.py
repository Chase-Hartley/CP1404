
from prac_06.guitar_storage import GuitarStorage


def main():
    guitars = []

    print("My guitars!")
    name = input("Enter the name of the guitar\n>>> ")
    while name != "":
        year = int(input("Please enter the year, the guitar was released\n>>> "))
        cost = float(input("Please enter the cost of your guitar\n>>>"))
        add_guitar = GuitarStorage(name, year, cost)
        guitars.append(add_guitar)
        print("{} ({}) : ${} added.".format(add_guitar.name, add_guitar.year, add_guitar.cost))
        name = input("Enter the next name of the guitar\n>>> ")

    # guitars.append(GuitarStorage("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(GuitarStorage("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        print("These are mine:")
        for i, guitar in enumerate(guitars):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name,
                                                                      guitar.year, guitar.cost, vintage))
    else:
        print("I can't afford new guitars.")





main()
