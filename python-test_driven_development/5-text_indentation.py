#!/usr/bin/python3

""" This script define"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text: text to check.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_char = [".", "?", ":"]
    result = ""
    for char in text:
        result += char
        if char in special_char:
            trimmed_result = result.strip()
            print(trimmed_result + "\n")
            result = ""

    if result.strip() != "":
        print(result.strip(), end="")
