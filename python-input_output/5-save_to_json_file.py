#!/usr/bin/python3

""" 5-save_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file in JSON format.

    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
