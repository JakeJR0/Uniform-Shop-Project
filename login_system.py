"""
This is a login system used to determine whether the user has the right details to login
"""

from werkzeug.security import generate_password_hash, check_password_hash
import pandas as pd



def login_system():
    """
    This is the login system.
    """
    count = 0
    logged_in = False

    while count < 3:
        # Gives the user 3 tries to get the user and pass right or they are logged out
        print("\nPlease login:\n")
        user = input("\nEnter username: ")
        password = input("\nEnter password: ")

        if login(user, password):
            logged_in = True
            break
        count = count + 1
        print("\nUsername / Password is incorrect.")

    return logged_in


def encrypt_pass(password):
    """
    This uses to encrypt the password using the sha256 method.
    """
    encrypt = generate_password_hash(password, "pbkdf2:sha256:1000")
    return encrypt


def read_user_data():
    """
    This is use to read the userdata from the csv.
    """
    try:
        passdetail = pd.read_csv("passdetail.csv")
    except FileNotFoundError:
        passdetail = pd.DataFrame({"Username": [], "Password": []})

    return passdetail


def valid_details(username, password, passdetail):

    """
    This is use to verifying the details that the user inputs.
    """
    usernames = [passdetail.loc[i, "Username"] for i in passdetail.index]
    if username in usernames:
        return False

    if 2 < len(username) <= 20:
        if 8 <= len(password) <= 25:
            return True
        return False
    return False

def signup(username, password):
    """
    This is the sign up system.
    """
    passdetail = read_user_data()
    print("Your detail:")
    print(f"Username:{username}")
    print(f"Password:{password}")

    if not valid_details(username, password, passdetail):
        return False

    data = [username, encrypt_pass(password)]
    passdetail.loc[len(passdetail.index)] = data
    passdetail.to_csv("passdetail.csv", index=False)
    print("Data accepted.")
    return True


def login(username, password):
    """
    This is the login system.
    """
    detail = read_user_data()
    for xyz in detail.index:
        username_ans = detail.loc[xyz, "Username"]
        password_ans = detail.loc[xyz, "Password"]
        if username == username_ans:
            if check_password_hash(password_ans, password):
                return True
    return False
