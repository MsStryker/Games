# -*- coding: utf-8 -*-
"""
This is a copy of the default.py file to be converted/updated using numpy

"""
from collections import Counter
from copy import deepcopy
from math import sqrt
from random import sample as random_sample
from string import ascii_uppercase

import numpy as np


class SudokuBoard(object):
    """Create a Sudoku Board of variable size

    The method will create the random sudoku Board
    of various size.
    """

    def __init__(self, size, level='easy', base_iterations=55):
        self.base = sqrt(size)
        if not (self.base).is_integer():
            raise ValueError('Please provide a number that has a square root.')
        if size > 25:
            raise ValueError('Please select a number 25 or below.')

        self.base = int(self.base)
        self.size = size
        self.base_iterations = base_iterations
        self.board_list = self.get_board_list()
        self.replacement_number = self.get_replacement_number(level)

        self.board = []

    def get_replacement_number(self, level):
        """Calculate replacement_number by level"""
        if level.lower() == 'easy':
            return int(self.size/4)
        elif level.lower() == 'medium':
            return int(self.size/3)
        elif level.lower() == 'hard':
            return int(self.size/2)

        return int(self.size/1.5)

    def _get_initial_list(self):
        """Create the initial list"""
        initial_list = []
        for i in range(1, self.size+1):
            initial_list.append(i)
        return initial_list

    def get_board_list(self):
        """Convert list greater than 9 to alpha numeric"""
        initial_list = self._get_initial_list()
        if len(initial_list) > 9:
            letters = list(ascii_uppercase[:(self.size - 9)])
            initial_list = initial_list[:9] + letters
        return initial_list

    def get_initial_matrix(self):
        """Create the matrix for the board
        
        TODO: convert this to a numpy array
        """
        board_list = self.board_list
        initial_matrix = [board_list]
        for i in range(1, self.size):
            rhs = board_list[i:]
            lhs = board_list[:i]
            new_list = rhs + lhs
            initial_matrix.append(new_list)

        return initial_matrix

    def get_full_board(self):
        """Get the full random board

        First, get the initial matrix and mutate rows
        and columns in the matrix. For this, we switch
        rows and columns that are within the base groups.

            ex. if the base is 3, we switch the following
            groups with each other:
                - 1, 2, 3
                - 4, 5, 6
                - 7, 8, 9
        """
        self.board = self.get_initial_matrix()
        for i in range(0, self.base_iterations):
            self.swap_columns()
            self.swap_rows()

        return self.board

    def swap_columns(self):
        """Swap the columns and return the board
        
        Using numpy swap the columns, where the following is an
        example of swapping the first and second column.
        
        TODO: a[:,[0,1]] = a[:,[1,0]]
        """
        board = self.board
        swap_list = range(0, self.size)
        for i in range(0, self.size, self.base):
            l_ind = i
            r_ind = i + self.base
            for j in range(self.base - 1):
                swap = random_sample(swap_list[l_ind:r_ind], 2)
                for k in range(0, self.size):
                    row = board[k]
                    row[swap[0]], row[swap[1]] = row[swap[1]], row[swap[0]]

    def swap_rows(self):
        """Swap the rows and return the board
        
        Using numpy swap the rows, where the following is an 
        example of swapping the first and second row.
        
        TODO: a[[0,1]] = a[[1,0]]
        """
        board = self.board
        swap_list = range(0, self.size)
        for i in range(0, self.size, self.base):
            l_ind = i
            r_ind = i + self.base
            for j in range(self.base - 1):
                swap = random_sample(swap_list[l_ind:r_ind], 2)
                board[swap[0]], board[swap[1]] = board[swap[1]], board[swap[0]]

    def get_playable_board(self):
        """Get the playable board

        Replace random values with `None` for the user.
        """
        board = self.get_full_board()
        playable_board = deepcopy(board)
        i = 0
        while i < self.replacement_number:
            point = random_sample(range(0, self.size), 2)
            if playable_board[point[0]][point[1]] is None:
                pass
            else:
                playable_board[point[0]][point[1]] = None
                i += 1

        return playable_board


def is_unique_list(board_list):
    """Check if items are unique excluding None"""
    items = Counter(board_list)
    items.pop(None, None)
    if len(set(items.values())) > 1:
        return False

    return True


def verify_sudoku_board(board):
    """Return boolean on if board passes"""
    size = len(board)
    # check rows
    for i in range(size):
        if not is_unique_list(board[i]):
            return False

    # check columns
    for i in range(size):
        column = []
        for j in range(size):
            column.append(board[i][j])

        if not is_unique_list(column):
            return False

    return True


if __name__ == '__main__':
    pass
