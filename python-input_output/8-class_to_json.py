#!/usr/bin/python3

"""8-class_to_json module"""


def class_to_json(obj):
    """
    Converts a Python object to a JSON serializable dictionary.

    Args:
        obj (object): The Python object to be converted.

    Returns:
        dict: A dictionary that can be serialized to JSON.

    Raises:
        (Include any specific exceptions this function might raise)

    Examples:
        >>> class_to_json({'key': 'value'})
        {'key': 'value'}

    Note:
        (Any additional notes about the function)
    """
    return obj.__dic__
