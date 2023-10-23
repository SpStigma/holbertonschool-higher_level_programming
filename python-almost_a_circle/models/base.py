#!/usr/bin/python3

"""base module"""


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
