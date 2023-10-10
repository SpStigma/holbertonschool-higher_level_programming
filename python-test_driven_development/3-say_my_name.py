#!/usr/bin/python3

""" This script define a fonction to print first name
    and last_name"""


def say_my_name(first_name, last_name=""):
    """
    Print my name is (first name) (last name)

    Args:
        first_name: Prénom
        last_name: Nom de famille
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
