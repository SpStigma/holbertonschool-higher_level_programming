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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a JSON file.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            list: An empty list if `list_objs` is None or empty;
            otherwise, None.
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        converted_objs = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(converted_objs)

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string into a Python object.

        Args:
            json_string (str): A string containing valid JSON data.

        Returns:
            object: The Python object represented by the JSON
            string. If the input
            string is empty or None, an empty list will be returned.
            if json_string is None or len(json_string) == 0:
            return []
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class with all attributes already set.

        Args:
            **dictionary: A dictionary containing the attributes
            and their values.

        Returns:
            A new instance of the class with attributes configured
            according to the dictionary.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        The filename is constructed using the class name:
          "<Class name>.json" (e.g., "Rectangle.json").
        If the file doesn’t exist, an empty list is returned.

        Returns:
            list: A list of instances of the current class.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                data = Base.from_json_string(file.read())
                instances = []
                for item in data:
                    instances.append(cls.create(**item))
                return instances
        except FileNotFoundError:
            return []
