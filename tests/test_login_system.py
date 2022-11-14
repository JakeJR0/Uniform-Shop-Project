"""
  This file is designed to test the login_system.py file to ensure that the functions
  within the file are working as expected.
"""

# Imports the required modules
import os
from werkzeug.security import check_password_hash

# Imports the login_system.py file to test the functions within it.

from login_system import encrypt_pass, login, signup

USER_DETAILS_FILE_NAME = "passdetail"

def test_encrypt_pass():
    """
      This function will run mutiple basic tests on the encrypt_pass function
      within the login_system.py file.

      This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    assert check_password_hash(encrypt_pass("password"), "password") is True, \
    "The function should encrypt the password correctly."

    assert check_password_hash(encrypt_pass("password"), "password1") is False, \
    "The function should encrypt the password correctly."

def test_signup():
    """
      This function will run mutiple basic tests on the signup function
      within the login_system.py file.

      This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    csv_file = f"{USER_DETAILS_FILE_NAME}.csv"

    if os.path.exists(csv_file):
        os.remove(csv_file)

    assert signup("Admin", "root_account") is True, \
    "The function should create a new account."

    assert signup("Admin", "root_account") is False, \
    "The function should not create a duplicated account."

    assert signup("User", "ddd") is False, \
    "The function should not create an account with a password shorter than 8 characters."

    assert signup("a", "d"*10) is False, \
    "The function should not create an account with a username shorter than 2 characters."

    assert signup("a"*21, "d"*10) is False, \
    "The function should not create an account with a username longer than 20 characters."

def test_login():
    """
      This function will run mutiple basic tests on the login function
      within the login_system.py file.

      This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    assert login("Admin", "root_account") is True, \
    "The function should login to an existing account."

    assert login("Admin", "root_account123") is False, \
    "The function should not login to an existing account with the wrong password."

    assert login("Admin1", "root_account") is False, \
    "The function should not login to a non-existing account."
