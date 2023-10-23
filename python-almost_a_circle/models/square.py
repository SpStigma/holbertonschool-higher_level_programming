#!/usr/bin/python3

"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A class representing a square.

    Args:
        size (int): The size of the square.
        x (int, optional): The x-coordinate of the
        square's position (default is 0).
        y (int, optional): The y-coordinate of the
        square's position (default is 0).
        id (int, optional): The identifier of the square (default is None).
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        The string includes the object's type, id,
        coordinates, and size.

        Returns:
            str: A formatted string representation
            of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
