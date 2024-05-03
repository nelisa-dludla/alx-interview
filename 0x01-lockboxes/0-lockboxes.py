#!/usr/bin/python3
'''
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    Checks if all boxes can be opened

    Args:
        boxes - A list of lists with int inside

    Return:
        True - If all boxes can be opened
        False - If not all boxes can be opened
    '''

    n = len(boxes)
    opened = set()
    opened.add(0)
    boxToBeChecked = [0]

    while boxToBeChecked:
        current_box = boxToBeChecked.pop()

        for key in boxes[current_box]:
            if key < n and key not in opened:
                opened.add(key)
                boxToBeChecked.append(key)

    if len(opened) == n:
        return True
    else:
        return False
