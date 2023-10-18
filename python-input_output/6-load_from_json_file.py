#!/usr/bin/python3

""" 6-load_from_json_file module """
import json


def load_from_json_file(filename):
    """
    Load JSON data from a file and return the parsed content.

    Args:
        filename (str): The name of the file to load JSON data from.

    Returns:
        dict: The parsed JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If there is an error in decoding JSON data.

    Example:
        >>> data = load_from_json_file('example.json')
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
