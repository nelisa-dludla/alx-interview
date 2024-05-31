#!/usr/bin/python3
'''
This script N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard
'''


import sys


def valid_position(board, row, col):
    '''
    Checks if queen can be placed on current
    position
    '''
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def print_solution(board):
    '''
    Prints out the solution
    '''
    solution = [[i, col] for i, col in enumerate(board)]
    print(solution)


def nqueens(n):
    '''
    Solves the nqueens problem
    '''
    board = [-1] * n
    row = 0
    col = 0

    while row < n:
        while col < n:
            if valid_position(board, row, col):
                board[row] = col
                col = 0
                break
            else:
                col += 1

        if board[row] == -1:
            if row == 0:
                return
            row -= 1
            col = board[row] + 1
            board[row] = - 1
        elif row == n - 1:
            print_solution(board)
            col = board[row] + 1
            board[row] = -1
        else:
            row += 1


def main():
    '''
    Main script
    '''
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        return

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        return

    if n < 4:
        print('N must be at least 4')
        return

    nqueens(n)


if __name__ == '__main__':
    main()
