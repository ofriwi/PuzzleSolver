import numpy as np
from PIL import Image
import Piece
import math
import HelpingFunction as HF
from Constants import *
import DistanceAnalysis as Dist
import Solver


class Board:
    """
    picture - picture's object
    board - nparray of arranged pieces
    pieces - nparray of pieces
    height, width - in pixels
    piece_height, piece_width - in pixels
    n, m - width and height (in # of pieces)
    solver - Solver object
    """

    # Constructor

    def __init__(self, picture):
        """
        Constructor
        :param: board numpy arr[n*n] of Pieces - the board 
        :return: 
        """
        # Initialize values
        self.picture = picture
        self.n = picture.n
        self.m = picture.m
        self.piece_height = picture.piece_height
        self.piece_width = picture.piece_width
        self.height = picture.height
        self.width = picture.width

        # Initialize board and pieces
        self.board = np.empty((self.n, self.m), dtype=object)  # board
        self.pieces = np.array(picture.pieces.copy())

        # Initialize solver
#        self.solver = Solver.Solver(self)

    # Image handling

    def show_solution(self):
        '''
        Print the proposed solution to screen
        :return: 
        '''
        HF.show_image(self.get_solution_array())

    def get_solution_array(self):
        '''
        Get nparray with proposed solution
        :return: nparray of the solution
        '''
        solved = np.empty(self.picture.img_arr.shape, self.picture.img_arr.dtype)
        for k in range(self.m):
            for l in range(self.n):
                solved[(k * self.piece_height):((k + 1) * self.piece_height), (l * self.piece_width):((l + 1) * self.piece_width), :] \
                    = self.board[k, l].matrix
        return solved

    # Solver

    def solve(self):
        # TODO
        return

    # Distances

    def get_distance_matrix(self):
        '''
        Get a distance matrix of the board
        :return: Distance matrix
        '''
        return Dist.get_distance_matrix(self.pieces, self.picture.name)

    # Pieces

    def get_piece_in_location(self, pos):
        '''
        Get a piece object in a location
        :param pos: position tuple
        :return: object if piece not empty, NO_PIECE otherwise
        '''
        if self.is_cell_empty(pos):
            return NO_PIECE
        else:
            return self.board[pos]

    def add_piece_in_position(self, pos, piece):
        '''
        Add a piece in certain position
        :param pos: position
        :param piece: piece object
        :return: 
        '''
        self.board[pos[0], pos[1]] = piece

    def add_piece_in_direction(self, pos, piece, direction):
        '''
        Add a piece in certain direction according to a position
        :param pos: position
        :param piece: the piece to add
        :param direction: TOP, RIGHT, LEFT or BOTTOM
        :return: 
        '''
        if direction == TOP:
            self.add_piece_in_position((pos[0] - 1, pos[1]), piece)
        if direction == LEFT:
            self.add_piece_in_position((pos[0], pos[1] - 1), piece)
        if direction == RIGHT:
            self.add_piece_in_position((pos[0], pos[1] + 1), piece)
        if direction == BOTTOM:
            self.add_piece_in_position((pos[0] + 1, pos[1]), piece)

    # Cells checking

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
        n = self.board.shape[0]
        m = self.board.shape[1]
        if 0 <= i < m and 0 <= j < n:
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

    def get_empty_directions_around(self, pos):
        '''
        Get the direction of empty pieces around as a list
        :param pos: piece's position
        :return: list of empty directions (i.e. [RIGHT, BOTTOM] for upper left corner)
        '''
        result = []
        i = pos[0]
        j = pos[1]
        if self.is_cell_empty((i - 1, j)):
            result.append(TOP)
        if self.is_cell_empty((i, j - 1)):
            result.append(LEFT)
        if self.is_cell_empty((i, j + 1)):
            result.append(RIGHT)
        if self.is_cell_empty((i + 1, j)):
            result.append(BOTTOM)
        return result
