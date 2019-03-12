"""Chase Hartley"""


def main():
    password = get_password()
    obscures_password(password)


def obscures_password(password):
    show_user = ""
    for i in range(password_length_checker(password)):
        show_user = "*" + show_user
    print(show_user)


def get_password():
    password = input("Please enter your password:"
                     "\npassword must be at least 6 characters long"
                     "\n>>> ")
    while password_length_checker(password) < 6:
        password = input("Incorrect password:"
                         "\npassword must be at least 6 characters long"
                         "\n>>> ")
    return password


"""Question: Why does 'i' say there is no 'local variable' when in a function but when in a blank program
there is no error"""


def password_length_checker(password):
    count = 0
    for i in password:
        count += 1
    return count


main()
