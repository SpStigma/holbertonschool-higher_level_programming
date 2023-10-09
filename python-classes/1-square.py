#!/usr/bin/python3

""" This script define a square with a private instance attribute."""


class Square:
    """ A class that represent a square. Who use the method of __init__
    to make a private attribute"""

    def __init__(self, size):
        self.__size = size
