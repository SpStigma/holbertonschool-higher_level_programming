#!/usr/bin/python3

""" This script define a square with a private instance attribute."""


class Square:
    """ A class that represent a square. Who use the method of __init__
    to make a private attribute who has some condition for size"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
