#!/usr/bin/python3

""" This script define a square with a private instance attribute."""


class Square:
    """ A class that represent a square. Who use the method of __init__
    to make a private attribute who has some condition for size and
    some methodes:
    to calculate the area..."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        for x in range(self.__size):
            print("#" * self.__size)
