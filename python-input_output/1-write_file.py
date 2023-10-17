#!/usr/bin/python3

""" 1-write_file module """


def write_file(filename="", text=""):
    """
    This module provides a function to write text to a file.

    Parameters:
        filename (str): The name of the file to be written.
        If not provided, an empty string will be used.
        text (str): The text to be written to the file.
        If not provided, an empty string will be used.

    Returns:
        int: The number of characters written to the file.

    Example:
        To write the text "Hello, World!" to a file named "output.txt",
        you can use the function like this:

        >>> write_file("output.txt", "Hello, World!")

    Note:
        If the file with the specified filename
        already exists, it will be overwritten.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
