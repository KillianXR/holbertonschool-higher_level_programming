#!/usr/bin/python3
"""
create a representation of pascal triangle
n: number of line
"""


def pascal_triangle(n):
    """
    create a representation of pascal triangle
    n: number of line
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) is not n:
        new_line = [1]

        for count in range(len(triangle[-1]) - 1):
            new_line.append(triangle[-1][count] + triangle[-1][count + 1])

        new_line.append(1)
        triangle.append(new_line)

    return triangle
