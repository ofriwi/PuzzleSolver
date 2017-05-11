import numpy as np
from PIL import Image

import DistanceAnalysis as Dist
import HelpingFunction as HF
import Piece
from Constants import *


class Board1:
    '''
    img_arr - nparray
    board - nparray of arranged pieces
    pieces - list of pieces (Attention - not nparray)
    height, width - in pixels
    piece_height, piece_width - in pixels
    n, m - width and height (in # of pieces)
    solver - Solver object
    '''

    # Constructor

    def __init__(self, image_address, n, m=0):
        '''
        Constructor
        :param: board numpy arr[n*n] of Pieces - the board 
        :return: 
        '''
        if m == 0:
            m = n
        # Initialize values
        self.n = n
        self.m = m
        img = Image.open(image_address).convert(GRAY)
        self.piece_height = int(math.ceil(img.size[1] / m))
        self.piece_width = int(math.ceil(img.size[0] / n))
        self.height = self.piece_height * m
        self.width = self.piece_width * n
        # Crop the image a little (so all pieces has the same size)
        img = img.crop((0, 0, self.width, self.height))

        # image to array
        self.img_arr = np.array(img)

        # Initialize board and pieces
        self.board = np.empty((n, m), dtype=object)  # board
        self.pieces = self.crop_image()

        # Initialize solver
#        self.solver = Solver.Solver(self)

    def crop_image(self):
        '''
        Crop the image and save the pieces in a list
        :return: list of pieces objects
        '''
        pieces = []
        for i in range(0, self.height, self.piece_height):
            for j in range(0, self.width, self.piece_width):
                pieces.append(Piece.Piece(self.img_arr[i:i+self.piece_height, j:j+self.piece_width].copy()))
        return pieces

    # Image handling

    def show_image(self):
        '''
        Print the original image
        :return: 
        '''
        HF.show_image(self.img_arr)

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
        solved = np.empty(self.img_arr.shape, self.img_arr.dtype)
        for k in range(self.m):
            for l in range(self.n):
                solved[(k * self.piece_height):((k + 1) * self.piece_height), (l * self.piece_width):((l + 1) * self.piece_width), :] \
                    = self.board[k, l].matrix
        return solved

    # Solver

    def solve(self):
        return

    # Pieces handling

    def get_distance_matrix(self):
        return Dist.get_distance_matrix(self.pieces)

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
