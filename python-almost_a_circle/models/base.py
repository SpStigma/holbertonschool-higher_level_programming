#!/usr/bin/python3

"""base module"""
import json


class Base:
    """
    Base class for creating objects with unique IDs.

    Attributes:
        __nb_objects (int): A class variable to keep
        track of the number of instances created.

    Args:
        id (int, optional): An optional argument to specify
        a custom ID. If not provided, a unique ID will be assigned.

    Attributes:
        id (int): The unique identifier for each instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An optional argument to specify a custom ID.
            If not provided, a unique ID will be assigned
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of the list of dictionaries.
                If the input list is None or empty, it returns "[]".
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
