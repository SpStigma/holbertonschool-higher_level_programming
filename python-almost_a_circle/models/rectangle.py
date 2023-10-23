#!/usr/bin/python3

""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle with specified dimensions and position.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int, optional): The x-coordinate of the
        top-left corner. Default is 0.
        y (int, optional): The y-coordinate of the
        top-left corner. Default is 0.
        id (int, optional): The unique identifier for
        the rectangle. Default is None.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner.
        y (int): The y-coordinate of the top-left corner.
        id (int): The unique identifier for the rectangle.

    Inherits from:
        Base: A base class providing a unique identifier.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance with specified dimensions and
        position.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner.
                Default is 0.
            y (int, optional): The y-coordinate of the top-left corner.
                Default is 0.
            id (int, optional): The unique identifier for the rectangle.
                Default is None.

        Raises:
            TypeError: If width, height, x, or y are not integers.
            ValueError: If width, height, x, or y are not within valid ranges..
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not within a valid range.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not within a valid range.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get the x-coordinate of the top-left corner.

        Returns:
            int: The x-coordinate.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the top-left corner.

        Args:
            value (int): The new x-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not within a valid range.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get the y-coordinate of the top-left corner.

        Returns:
            int: The y-coordinate.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the top-left corner.

        Args:
            value (int): The new y-coordinate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not within a valid range.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """
        Display the rectangle using '#' characters.

        Prints a visual representation of the rectangle
        using '#' characters.
        The number of '#' characters in each row is equal
        to the width of the rectangle.
        """
        if self.y > 0:
            for _ in range(0, self.y):
                print()

        for i in range(0, self.height):
            if self.x > 0:
                print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        The string includes the object's type, id,
        coordinates, width, and height.

        Returns:
            str: A formatted string representation
            of the Rectangle.
        """
        r = "[Rectangle] "
        return f"{r}({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        """
        Update attributes of the Rectangle.

        This method takes a variable number of arguments. The order
        of arguments is important and should be as follows:
        1st argument: id (int)
        2nd argument: width (int)
        3rd argument: height (int)
        4th argument: x (int)
        5th argument: y (int)

    Args:
        *args: Variable number of arguments in the specified order.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
