#!/usr/bin/python3
''' Soluton to interview question Island Perimeter
'''

def island_perimeter(grid):
    '''Returns the perimeter of the "grid"
    '''
    # Store visited cells
    visited = set()
    grid_length = len(grid)

    def explore_island(row, col):
        '''Checks if cell is part of the island or sea
        '''
        if row >= grid_length or col >= grid_length or row < 0 or col < 0 or grid[row][col] == 0:
                return 1
        if (row, col) in visited:
            return 0

        visited.add((row, col))

        # Right
        perimeter = explore_island(row, col + 1)
        # Down
        perimeter += explore_island(row + 1, col)
        # Left
        perimeter += explore_island(row, col - 1)
        # Up
        perimeter += explore_island(row - 1, col)

        return perimeter

    for row in range(grid_length):
        for col in range(grid_length):
            if grid[row][col]:
                return explore_island(row, col)
