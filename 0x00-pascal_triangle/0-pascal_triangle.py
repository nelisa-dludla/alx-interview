#!/usr/bin/python3
'''
This function returns a list of lists of integers
representing the Pascal’s triangle of n
'''


def pascal_triangle(n):
    '''
    Computes the pascal triangle

    Args:
        n: number of rows to be computed

    Returns:
        A list of all the computed rows
    '''
    if n <= 0:
        return []

    triangle = []

    for loop in range(n):
        if loop == 0:
            new_row = calc_new_row(triangle)
        else:
            new_row = calc_new_row(triangle[loop - 1])

        triangle.append(new_row)

    return triangle


def calc_new_row(prev_row):
    '''
    A helper function that helps compute the values for a new row

    Args:
        prev_row: The previous row/value in the list

    Returns:
        A newly computed row
    '''
    if not prev_row:
        return [1]

    prev_row_copy = prev_row[:]

    new_row = []
    prev_row_copy.insert(0, 0)
    prev_row_copy.insert(len(prev_row_copy), 0)
    i = 0

    for i in range(len(prev_row_copy)):
        if i + 2 > len(prev_row_copy):
            break

        result = prev_row_copy[i] + prev_row_copy[i + 1]
        new_row.append(result)

    return new_row
