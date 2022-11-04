"""
This program is use to ask the client's detail
for the measuring service and validate the data of it.
"""
from datetime import datetime
import re
import pandas as pd


def f_name_vali(f_name=""):
    """
    This function is use for validating the first name.
    """
    # Gets the type of f_name
    if isinstance(f_name, bool):
        return False
    if not isinstance(f_name, str):
        f_name = str(f_name)
    # Validate the f_name
    if len(f_name) > 2 and len(f_name) <= 20:
        if f_name.isalpha() is True:
            print("First name accepted.")
            return True

        print("Invalid First name, Please try again.")
        return False

    print("Invalid First name, Please try again.")
    return False


def l_name_vali(l_name=""):
    """
    This function is use for validating the last name.
    """
    # gets the type of l_name
    if isinstance(l_name, bool):
        return False
    if not isinstance(l_name, str):
        l_name = str(l_name)
    # validate l_name
    if len(l_name) > 2 and len(l_name) <= 30:
        if l_name.isalpha() is True or re.match("^[a-zA-Z-]*$", l_name):
            print("Last name accepted.")
            return True

        print("Invalid last name, Please try again.")
        return False

    print("Invalid last name, please try again.")
    return False


def size_vali(size=0):
    """
    This function is use for validating the size variable.
    """
    # Validating size
    if 6 <= size <= 22:
        if (size % 2) == 0:
            print("Size accepted.")
            return True

        print("Invalid size, Please try again. ")
        return False

    print("Invalid size, Please try again. ")
    return False


def date_vali(date1=""):
    """
    This function is use for validating the date.
    """
    # trying the date is correct or not
    try:
        date1 = datetime.strptime(date1, "%d/%m/%Y")
        date1 = date1.date()
    except ValueError:
        print("Invalid date, please try again.")
        return False

    # validate the date
    tdy = datetime.now().date()
    if date1 >= tdy or date1 is tdy:
        print("Date accepted")
        return True

    print("Invalid date, Please try again.")
    return False


def measur_serv():
    """
    This is the main running function for the program.
    """
    # create the loop for the f_name and get f_name
    valid = False
    while not valid:
        f_name = input("\nPlease enter your First name: ")
        valid = f_name_vali(f_name)

    # create the loop for the l_name and get l_name
    valid2 = False
    while not valid2:
        l_name = input("\nPlese enter your last name: ")
        valid2 = l_name_vali(l_name)

    # create the loop for the size and get size
    valid3 = False
    while not valid3:
        try:
            size = int(input("\nPlease enter your size: "))
            valid3 = size_vali(size)
        except ValueError:
            print("Invalid number, please enter a number.")
            valid3 = False

    # create the loop for the date and get date1
    valid4 = False
    while not valid4:
        date1 = input("Input your date as (DD/MM/YYYY): ")
        valid4 = date_vali(date1)

    dataf = None

    # open or create the dataframe
    try:
        dataf = pd.read_csv("measur_serv.csv")
    except FileNotFoundError:
        dataf = pd.DataFrame(
            {
                "First_name": [],
                "Last_name": [],
                "Size": [],
                "Date": [],
            }
        )

    # comfirm the details are correct.
    print("\nAdded User with details:")
    print(f"First Name: {f_name}")
    print(f"Last Name: {l_name}")
    print(f"Size: {size}")
    print(f"Date: {date1}")
    valid5 = False
    while not valid5:
        try:
            ans = int(input("\nIs this correct?, 1 for yes. 2 for no\n"))
        except ValueError:
            print("Invalid number, please try again")
        if ans == 1:
            data = [f_name, l_name, size, date1]
            dataf.loc[len(dataf.index)] = data
            dataf.to_csv("measur_serv.csv", index=False)
            print("Data accepted.")
            valid5 = "2147483647"
        elif ans == 2:
            measur_serv()
        else:
            print("Invalid number, please try again")


# Start the program.
if __name__ == "__main__":
    measur_serv()
