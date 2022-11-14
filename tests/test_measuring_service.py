"""
  This file is designed to test the measuring_service.py file to ensure that the functions
  within the file are working as expected.
"""

# Imports the required modules
from datetime import datetime, timedelta

import pytest

# Imports the measuring_service.py file to test the functions within it.
from measuring_service import date_vali, f_name_vali, l_name_vali


def test_f_name_vali_basic():
    """
      This function will run mutiple basic tests on the f_name_vali function
      within the measuring_service.py file.

      This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    # Tests if the function accepts a 4 letter name as a valid first name.
    assert f_name_vali("John") is True, \
    "The function should accept a 4 letter name as a first name."
    # Tests if the function accepts a 9 letter name as a valid first name.
    assert f_name_vali("Johnathan") is True, \
    "The function should accept a 9 letter name as a first name."
    # Tests if the function does not accept a 1 letter name as a valid first name.
    assert f_name_vali("J") is False, \
    "The function should not accept a 1 letter name as a first name."
    # Tests if the function does not accept a 2 letter name as a valid first name.
    assert f_name_vali("Jo") is False, \
    "The function should not accept a 2 letter name as a first name."
    # Tests if the function does not accept a 31 letter name as a valid first name.
    assert f_name_vali("J" * 31) is False, \
    "The function should not accept a 31 letter name as a first name."

def test_f_name_vali():
    """
      This function will run mutiple tests on the f_name_vali function
      within the measuring_service.py file.

      This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    # Tests if the function allows probhited characters in the first name.
    assert f_name_vali("John!") is False, \
    "The function should not accept a name with a ! in it."

    assert f_name_vali("John@") is False, \
    "The function should not accept a name with a @ in it."

    # Tests if the function checks if the first name has any numbers in it.
    assert f_name_vali("John1") is False, \
    "The function should not accept a name with a 1 in it."

    # Tests if the function checks if the first name has characters in it.
    assert f_name_vali("123456789") is False, \
    "The function should not accept a name with only numbers in it."

    assert f_name_vali("!$%*$£") is False, \
    "The function should not accept a name with only special characters in it."

    # Tests if the function checks if the first name is a string.
    assert f_name_vali(1) is False, \
    "The function should not accept a number as a first name."

    assert f_name_vali(1.1) is False, \
    "The function should not accept a float as a first name."

    assert f_name_vali(True) is False, \
    "The function should not accept a boolean as a first name."


def test_l_name_vali_basic():
    """
      This function will run mutiple basic tests on the l_name_vali function
      within the measuring_service.py file.

      This will ensure that the function acts as expected to ensure that the behavior is correct.
    """
    # Tests if the function accepts a 5 letter name as a valid last name.
    assert l_name_vali("Smith") is True, \
    "The function should accept a 5 letter name as a last name."
    # Tests if the function accepts a 8 letter name as a valid last name.
    assert l_name_vali("Smithers") is True, \
    "The function should accept a 8 letter name as a last name."
    # Tests if the function accepts a - in the last name.
    assert l_name_vali("Smith-Jones") is True, \
    "The function should accept '-' in the last name."
    # Tests if the function does not accept a 1 letter name as a valid last name.
    assert l_name_vali("S") is False, \
    "The function should not accept a 1 letter name as a last name."
    # Tests if the function does not accept a 2 letter name as a valid last name.
    assert l_name_vali("Sm") is False, \
    "The function should not accept a 2 letter name as a last name."
    # Tests if the function does not accept a 31 letter name as a valid last name.
    assert l_name_vali("S" * 31) is False, \
    "The function should not accept a 31 letter name as a last name."

def test_l_name_vali():
    """
      This function will run mutiple tests on the l_name_vali function
      within the measuring_service.py file.

      This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    # Tests if the function allows probhited characters in the last name.
    assert l_name_vali("Smith!") is False, \
    "The function should not accept a name with a ! in it."

    assert l_name_vali("Smith@") is False, \
    "The function should not accept a name with a @ in it."

    # Tests if the function checks if the last name has any numbers in it.
    assert l_name_vali("Smith1") is False, \
    "The function should not accept a name with a 1 in it."

    # Tests if the function checks if the last name has characters in it.
    assert l_name_vali("123456789") is False, \
    "The function should not accept a name with only numbers in it."

    assert l_name_vali("!$%*$£") is False, \
    "The function should not accept a name with only special characters in it."

    # Tests if the function checks if the last name is a string.
    assert l_name_vali(1) is False, \
    "The function should not accept a number as a last name."

    assert l_name_vali(1.1) is False, \
    "The function should not accept a float as a last name."

    assert l_name_vali(True) is False, \
    "The function should not accept a boolean as a last name."

def test_date_vali_basic():
    """
        This function will run basic mutiple tests on the date_vali function
        within the measuring_service.py file.

        This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    # The function should accept today's date
    today = datetime.now()
    day, month, year = today.day, today.month, today.year
    assert date_vali(f"{day}/{month}/{year}") is True, \
    "The function should accept today's date."

    # The function should accept tomorrow's date
    tomorrow = today + timedelta(days=1)
    day, month, year = tomorrow.day, tomorrow.month, tomorrow.year
    assert date_vali(f"{day}/{month}/{year}") is True, \
    "The function should accept tomorrow's date."

    # The function should rejects yesterday's date
    yesterday = today - timedelta(days=1)
    day, month, year = yesterday.day, yesterday.month, yesterday.year
    assert date_vali(f"{day}/{month}/{year}") is False, \
    "The function should reject yesterday's date."

def test_date_vali():
    """
        This function will run mutiple tests on the date_vali function
        within the measuring_service.py file.

        This will ensure that the function acts as expected to ensure that the behavior is correct.
    """

    # The function should reject the date of 1/1/1
    assert date_vali("1/1/1") is False, \
    "The function should reject the date 1/1/1."

    # The function should reject the date of 1/1/10000
    assert date_vali("1/1/10000") is False, \
    "The function should reject the date 1/1/10000."

    # Gets today's datetime object
    today = datetime.now()

    # Gets the day, month and year from the datetime object
    day, month, year = str(today.day), str(today.month), str(today.year)

    assert date_vali(f"{day}, {month}, {year}") is False, \
        "The function should reject the date formatted incorrectly."

    # Ensures that a TypeError is raised if an int is passed to the function
    with pytest.raises(TypeError):
        assert date_vali(234) is False, \
        "The function should reject a int."

    # Ensures that a TypeError is raised if an float is passed to the function
    with pytest.raises(TypeError):
        assert date_vali(1.1) is False, \
        "The function should reject the date formatted as a float."

    # Ensures that a TypeError is raised if an boolean is passed to the function
    with pytest.raises(TypeError):
        assert date_vali(True) is False, \
        "The function should reject the boolean"

    # Calculates the date in a year's time
    next_year = today + timedelta(days=365)

    assert date_vali(f"32/10/{next_year.year}") is False, \
        f"The function should reject the date 32/10/{next_year.year}"

    assert date_vali(f"31/2/{next_year.year}") is False, \
        f"The function should reject the date 32/10/{next_year.year}"
