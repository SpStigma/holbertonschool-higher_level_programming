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

    def update(self, *args, **kwargs):
        """
        Update attributes of the Square.

        This method takes a variable number of arguments.
        The order of arguments
        is important and should be as follows:
        1st argument: id (int)
        2nd argument: size (int)
        3rd argument: x (int)
        4th argument: y (int)

        Args:
            *args: Variable number of arguments in the specified order.
            **kwargs: Keyworded arguments where each key represents an
            attribute.
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            self.id = kwargs.get('id', self.id)
            self.size = kwargs.get('size', self.size)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
