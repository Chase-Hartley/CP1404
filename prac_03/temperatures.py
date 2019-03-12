"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():

    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            get_fahrenheit()
        elif choice == "F":
            get_celsius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_celsius():
    fahrenheit = float(input("fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9.0
    print("Result: {:.2f} C".format(celsius))
    # Hint: celsius = 5 / 9 * (fahrenheit - 32)
    # Remove the "pass" statement when you are done. It's a placeholder.


def get_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


main()
