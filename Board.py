import numpy as np

import DistanceAnalysis as Dist
import HelpingFunction as HF
from Constants import *


class Board:
    """
    picture - picture's object
    _board - nparray of arranged pieces
    _board_indexes - nparray of assigned pieces' indexes
    _pieces - nparray of pieces
    height, width - in pixels
    piece_height, piece_width - in pixels
    n, m - width and height (in # of pieces)
    _indexes - all unassigned pieces' indexes
    _distance_matrix - D
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
        self._board = np.empty((self.n, self.m), dtype=object)  # board
        self._board_indexes = np.ones((self.n, self.m), int) * -1
        self._indexes = list(range(self.n * self.m))
        self._pieces = np.array(picture.pieces)

        # Initialize solver
        # self.solver = Solver.Solver(self)

    # Image handling

    def show_solution(self):
        """
        Print the proposed solution to screen
        :return: 
        """
        HF.show_image(self.get_solution_array())

    def show_solution_print_cost(self):
        self.show_solution()
        self.total_cost()

    def get_solution_array(self):
        """
        Get nparray with proposed solution
        :return: nparray of the solution
        """
        solved = np.empty(self.picture.img_arr.shape, self.picture.img_arr.dtype)
        for k in range(self.m):
            for l in range(self.n):
                if self._board_indexes[k, l] == -1:
                    solved[(k * self.piece_height):((k + 1) * self.piece_height)
                        , (l * self.piece_width):((l + 1) * self.piece_width)] = np.zeros((
                        self.piece_height, self.piece_width))
                else:
                    solved[(k * self.piece_height):((k + 1) * self.piece_height)
                        , (l * self.piece_width):((l + 1) * self.piece_width)] \
                        = self._board[k, l].matrix
        return solved

    # Distances

    def get_distance_matrix(self):
        """
        Get a distance matrix of the board
        :return: Distance matrix
        """
        return self.picture.distance_matrix

    def total_cost(self):
        total_cost = 0
        for i in range(self.n):
            for j in range(self.m):
                if not j == self.m - 1:
                    total_cost += Dist.get_border_distance(self._board[i, j].get_side(
                        RIGHT), self._board[i, j + 1].get_side(
                        LEFT))
                if not i == self.n - 1:
                    total_cost += Dist.get_border_distance(self._board[i, j].get_side(
                        BOTTOM), self._board[i + 1, j].get_side(TOP))
        if DEBUG:
            print('sol_cost = ' + str(total_cost))
        return total_cost
    # Pieces

    def get_piece_index_in_position(self, pos):
        """
        Get a piece object in a location
        :param pos: position tuple
        :return: piece index in pos
        """
        return self._board_indexes[pos]

    def get_piece_obj_in_position(self, pos):
        """
        Get a piece object in a location
        :param pos: position tuple
        :return: object if piece not empty, NO_PIECE otherwise
        """
        if self.is_cell_empty(pos):
            return NO_PIECE
        else:
            return self._board[pos]

    def add_piece_index_in_position(self, pos, piece_index):
        """
        Add a piece in certain position
        :param pos: position
        :param piece_index: piece index
        :return: 
        """
        self._board[pos[0], pos[1]] = self._pieces[piece_index]
        self._board_indexes[pos[0], pos[1]] = piece_index
        self._indexes.remove(piece_index)

    def get_position_in_direction(self, pos, direction):
        '''
        Get a tuple of the position in direction to another position
        :param pos: 
        :param direction: 
        :return: 
        '''
        if direction == TOP:
            return pos[0] - 1, pos[1]
        if direction == LEFT:
            return pos[0], pos[1] - 1
        if direction == RIGHT:
            return pos[0], pos[1] + 1
        if direction == BOTTOM:
            return pos[0] + 1, pos[1]
        return None

    def get_unassigned_cells(self):
        """
        Get list of all unassigned indexes
        :return: list
        """
        return self._indexes

    def add_piece_index_in_direction(self, pos, piece_index, direction):
        """
        Add a piece in certain direction according to a position
        :param pos: position
        :param piece_index: the piece to add
        :param direction: TOP, RIGHT, LEFT or BOTTOM
        :return: 
        """
        self.add_piece_index_in_position(self.get_position_in_direction(pos, direction), piece_index)

    def is_puzzle_completed(self):
        """
        Does the puzzle solved?
        :return: True if no unassigned piece is left
        """
        return len(self._indexes) == 0

    # Cells checking

    def is_cell_exist(self, pos):
        """
        1 if the cell exsists
        :param pos: position tuple
        :return: 
        """
        i = pos[0]
        j = pos[1]
        n = self._board.shape[0]
        m = self._board.shape[1]
        if 0 <= i < m and 0 <= j < n:
            return 1
        return 0

    def is_cell_empty(self, pos):
        """
        1 if cell is empty
        :param pos: position tuple
        :return: 
        """
        i = pos[0]
        j = pos[1]
        if self.is_cell_exist((i, j)):
            if self._board[i, j] is None:
                return 1
        return 0

    def is_cell_filled(self, pos):
        """
        1 if cell is not empty
        :param pos: position tuple
        :return: 
        """
        i = pos[0]
        j = pos[1]
        if self.is_cell_exist((i, j)):
            if self._board[i, j] is not None:
                return 1
        return 0

    def number_of_empty_pieces_around(self, pos):
        """
        Get number of empty pieces around a piece
        :param pos: position tuple
        :return: number of empty pieces
        """
        return len(self.get_empty_positions_around(pos))

    def get_empty_positions_around(self, pos):
        """
        Get empty pieces around a piece
        :param pos: position tuple
        :return: list of indexes (as (i, j))
        """
        indexes = []
        for cell in self.get_positions_around(pos):
            if self.is_cell_empty(cell):
                indexes.append(cell)
        return indexes

    def get_positions_around(self, pos):
        """
        Get all pieces around a piece
        :param pos: position tuple
        :return: list of indexes (as (i, j))
                    Ordered: T, L, R, B
        """
        i = pos[0]
        j = pos[1]
        indexes = []
        for cell in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
            if self.is_cell_exist(cell):
                indexes.append(cell)
        return indexes

    def get_empty_directions_around(self, pos):
        """
        Get the direction of empty pieces around as a list
        :param pos: piece's position
        :return: list of empty directions (i.e. [RIGHT, BOTTOM] for upper left corner)
        """
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
