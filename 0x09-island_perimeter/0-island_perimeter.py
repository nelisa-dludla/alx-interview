#!/usr/bin/python3
''' Soluton to interview question Island Perimeter
'''


def island_perimeter(grid):
    '''Returns the perimeter of the "grid"
    '''
    # Check if grid is valid
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with all 4 sides
                perimeter += 4
                # Check cell above for land
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                # Check cell on the left for land
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter
