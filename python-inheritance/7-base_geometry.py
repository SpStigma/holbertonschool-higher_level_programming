#!/usr/bin/python3

""" 5-base_geometry """


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class currently doesn't have any specific functionality
    and is intended to be used as a base for more specialized geometry classes.

    Methods:
        (None)
    """
    pass

    def area(self):
        """
        Calculate the area of géometry (not implemented).

        Raises:
            Exception: Indicates that the method is not implemented.

        Returns:
            None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
