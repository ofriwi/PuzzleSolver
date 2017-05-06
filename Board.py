import numpy as np


class Board:

    def __init__(self, board):
        '''
        Constructor
        :param board: numpy arr[n*n] of Pieces - the board 
        :return: 
        '''
        self.board = board

    def is_cell_exist(self, pos):
        '''
        1 if the cell exsists
        :param board: 
        :param i: 
        :param j: 
        :return: 
        '''
        i = pos[0]
        j = pos[1]
        n = len(self.board)
        if 0<=i<n and 0<=j<n:
            return 1
        return 0

    def is_cell_empty(self, pos):
        '''
        1 if cell is empty
        :param board: 
        :param i: 
        :param j: 
        :return: 
        '''
        i = pos[0]
        j = pos[1]
        if self.is_cell_exist((i, j)):
            if self.board[i, j] is None:
                return 1
        return 0

    def is_cell_filled(self, pos):
        '''
        1 if cell is not empty
        :param board: 
        :param i: 
        :param j: 
        :return: 
        '''
        i = pos[0]
        j = pos[1]
        if self.is_cell_exist((i, j)):
            if self.board[i, j] is not None:
                return 1
        return 0

    def number_of_empty_pieces_around(self, pos):
        '''
        Get number of empty pieces around a piece
        :param board: game board(as np array)
        :param i: row
        :param j: col
        :return: number of empty pieces
        '''
        return len(self.get_empty_pieces_around(pos))

    def get_empty_pieces_around(self, pos):
        '''
        Get empty pieces around a piece
        :param i: row
        :param j: col
        :return: list of indexes (as (i, j))
        '''
        indexes = []
        for cell in self.get_pieces_around(pos):
            if self.is_cell_empty(cell):
                indexes.append(cell)
        return indexes

    def get_pieces_around(self, pos):
        '''
        Get all pieces around a piece
        :param i: row
        :param j: col
        :return: list of indexes (as (i, j))
                    Ordered: T, L, R, B
        '''
        i = pos[0]
        j = pos[1]
        indexes = []
        for cell in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
            if self.is_cell_exist(cell):
                indexes.append(cell)
        return indexes
