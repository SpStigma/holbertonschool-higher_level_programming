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
