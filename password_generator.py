import random
import string
# import os
# import time
from click import pause
from title import title


title()
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")  # Letters, numbers & symbols


print("---------------------------------------------------------------------\n")  # Title

# -----MAIN PROGRAM-----
while True:
    # Lenght of the password and input type checker
    while True:
        password_lenght = input("Please specify the lenght of the password: ")

        try:
            password_lenght = int(password_lenght)
            break
        except ValueError:
            print("That doesn't seem to be a valid lenght.")

    def passwordGenerator():

        # Randomly shuffles the characters
        random.shuffle(characters)

        # Picking the random characters from the list
        password = [random.choice(characters) for _ in range(password_lenght)]
        # Shuffling the resultant password
        random.shuffle(password)

        # Converting the list to a string and printing the list
        print("\nYour password is: ", "".join(password))

    # Invoking the function
    passwordGenerator()
    print("---------------------------------------------------------------------")

    # Asking the user wants to generate another password
    wish_to_continue = input('''\nPLEASE NOTE THAT THE GENERATED PASSWORDS WON'T BE SAVED, BE SURE TO COPY YOUR PASSWORD BEFORE EXITING!
    \nDo you want to generate another password? [Y/N]: ''')
    print("\n")
    if wish_to_continue not in ["y", "yes", "Y", "Yes"]:
        pause("\nEnjoy your secure password ^-^! Press any key to exit...")
        break
