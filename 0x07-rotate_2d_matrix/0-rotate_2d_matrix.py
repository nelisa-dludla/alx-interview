#!/usr/bin/python3
'''Contains rotate_2d_matrix(matrix)
'''


def rotate_2d_matrix(matrix):
    '''Rotates a 2D matrix 90 degrees
    '''
    left = 0
    right = len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top = left
            bottom = right

            # Top Left -> Temp
            temp = matrix[top][left + i]
            # Bottom Left -> Top Left
            matrix[top][left + i] = matrix[bottom - i][left]
            # Bottom Right -> Bottom Left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # Top Right -> Bottom Right
            matrix[bottom][right - i] = matrix[top + i][right]
            # Temp -> Top Right
            matrix[top + i][right] = temp
        # Move to inner space
        left += 1
        right -= 1
