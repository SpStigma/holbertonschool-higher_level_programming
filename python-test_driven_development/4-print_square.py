#!/usr/bin/python3

""" This script define a fonction to print a square."""


def print_square(size):
    """
    Print a square
    
    Args:
        size: The size of square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
