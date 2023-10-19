#!/usr/bin/python3

"""12-pascal_triangle module """


def pascal_triangle(n):
    """
    Generate a Pascal's triangle up to the specified number of rows.

    Args:
        n (int): The number of rows to generate in the Pascal's triangle.

    Returns:
        list of list: A list of lists representing Pascal's
        triangle up to 'n' rows.
        Each inner list contains the coefficients for a specific row.

    Raises:
        ValueError: If 'n' is not a positive integer.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    matrix = [[1]]
    """génère nouvelle ligne a chaque itération"""
    for _ in range(1, n):
        """ Initialise a 1 la première case"""
        row = [1]
        """ recupère la dernière ligne de la matrix """
        prev_row = matrix[-1]
        """ itère les valeurs sauf le premier"""
        for i in range(1, len(prev_row)):
            """ fais les opérations """
            row.append(prev_row[i - 1] + prev_row[i])
        """ ajoute 1 a la fin """
        row.append(1)
        """ ajoute la ligne a matrix """
        matrix.append(row)
    return matrix
