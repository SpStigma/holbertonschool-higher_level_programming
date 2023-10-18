#!/usr/bin/python3

""" 4-from_json_string module"""
import json


def from_json_string(my_str):
    """
    Deserialize a JSON formatted string into a Python object.

    Args:
        my_str (str): A JSON formatted string.

    Returns:
        obj: The Python object deserialized from the input string.

    Raises:
        JSONDecodeError: If the input string is not valid JSON.

    Example:
        >>> from_json_string('{"key": "value"}')
        {'key': 'value'}
    """
    return json.loads(my_str)
