"""
   This is the main file for the program
"""
from measuring_service import measur_serv
from cleaned_menu import school_menu
from login_system import login_system, signup


def main_menu():
    """
    User can navigate through the main menu using this function
    """

    logged_in = login_system()

    if not logged_in:
        print("\nAuthorization Failed.")
        return

    # This creates menu options
    output = "\nWelcome to the school uniform system!\n"
    output += "\nOption 1: Measuring Service"
    output += "\nOption 2: Uniform"
    output += "\nOption 3: Sign up"
    while True:
        try:
            # This displays the menu options
            print(output)
            choice = int(input("\nUser Choice: "))
            if choice == 1:
                # option 1 takes you to the measuring service
                measur_serv()
            elif choice == 2:
                # option 2 takes you to the uniform
                school_menu()
            elif choice == 3:
                # option 3 takes you to the sign up system.
                username = input("\nEnter your username: ")
                passw = input("\nEnter your password: ")
                signup(username,passw)
            else:
                continue
            # This creates data validation
        except ValueError:
            print("Incorrect")
            # Lets the user know that they are incorrect

if __name__ == "__main__":
    main_menu()
