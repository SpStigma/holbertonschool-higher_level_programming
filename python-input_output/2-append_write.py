#!/usr/bin/python3

""" 2-append_write module """


def append_write(filename="", text=""):
    """
        Append text to a file.

        Args:
            filename (str): The name of the file to which
            text will be appended.
            text (str): The text to be appended to the file.

        Returns:
            int: The number of characters written to the file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            PermissionError: If the user does not have
            permission to write to the file.

        Example:
            >>> append_write("example.txt", "This is a test.")
            14
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
