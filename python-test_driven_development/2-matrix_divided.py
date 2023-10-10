#!/usr/bin/python3

""" This script define a fonction to divide by div a matrix"""


def matrix_divided(matrix, div):
    """
    divise a matrix by div.

    Args:
        matrix: The matrix
        div: The number to divide the matrix

    Return:
        The new matrix divided.
    """
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError("matrix must be a matrix (list of lists)\
                            of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        result.append(new_row)
    return result
