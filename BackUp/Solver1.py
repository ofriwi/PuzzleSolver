import Board
import DistanceAnalysis as Dist
import HelpingFunction as HF
import hungarian as Hungarian
from Constants import *
import numpy as np


class Solver1:
    '''
    picture - Picture object
    board - Board object
    D - distances matrix
    pieces_set - a set (list) of all the pieces (I in the article)
    current_cost - cost of the current preposed solution
    '''

    # TODO remove all pieces_set references
    # Main solver
    def solve(self):
        # TODO
        #for k in range(self.board.height):
         #   for l in range(self.board.width):
          #      for index in range(len(self.board.pieces)):
        k = 0
        l = 0
        index = 0
        self.single_solution((k, l), index)

    def single_solution(self, pos, piece_index):
        '''
        Try a single solution
        :param pos: the position to build around
        :param piece_index: the index of the piece in the position
        :return: 
        '''

        # init
        self.board = Board.Board(self.picture)
        # self.pieces_set = self.board.pieces.tolist()
        self.indexes = list(range(len(self.board._pieces)))
        self.current_cost = 0

        # Lines 5 - 7
        #self.pieces_set.remove(cur_piece)
        self.indexes.remove(piece_index)
        self.board.add_piece_in_position(pos, piece_index)

        self.build_around(pos)

        # TODO : save cost

        self.board.show_solution()

    def build_around(self, pos):
        '''
        Build the 4 pieces around a piece.
        :param pos: the position to build around
        :param piece_index: the index of the piece in the position
        :return: 
        '''
        piece_index = self.board._board[pos].get_index()
        cur_piece = self.board._pieces[piece_index]

        # Lines 8 - 9
        empty_directions = self.board.get_empty_directions_around(pos)
        assign = self.get_hungarian(piece_index, empty_directions)
        cost = self.get_cost(piece_index, assign)
        self.current_cost += cost

        # Lines 10 - 11
        self.assign_pieces(pos, assign)

        if not len(self.indexes) == 0:
            next_pos = self.get_next_position_to_match(pos)
            if next_pos is not None:
                self.build_around(next_pos, self.board._board[next_pos])

    # Constructor
    def __init__(self, picture):
        self.picture = picture
        #self.pieces_set = []
        self.indexes = []
        self.board = Board.Board(picture)
        self.D = self.board.get_distance_matrix()
        self.current_cost = 0
        self.solve()

    # Lines 8-9
    def get_hungarian(self, piece_index, valid_directions):
        '''
        Get the hungarian arrangement around a piece
        :param piece_index: the piece's index
        :return: list of tuples (index, direction) where index is the index of the matching piece 
            and the direction is the direction relative to the piece
        '''
        H = HF.tuple_list_to_2d(self.D[piece_index, self.indexes])
        hungarian = Hungarian.Hungarian(H)
        hungarian.calculate()
        results = [(self.indexes[index], direction) for (index, direction) in hungarian.get_results()]
        return self.take_valid_direction(results, valid_directions)

    def get_cost(self, piece_index, hungarian):
        '''
        Get the cost of a match using hungarian
        :param piece_index: current piece's index
        :param hungarian: matching distance from hungarian
        :return: cost
        '''
        return sum(self.D[piece_index, piece][direction] for (piece, direction) in hungarian)

    def assign_pieces(self, cur_pos, assign):
        for (index, direction) in assign:
            self.board.add_piece_in_direction(cur_pos, self.board._pieces[index], direction)
            # self.pieces_set.remove(self.board.pieces[index])
            self.indexes.remove(index)

    # Line 13
    def get_next_position_to_match(self, cur_location):
        '''
        Get index for the next piece to match, as tuple.
        The next piece is an empty piece around the current piece with maximum empty neightbours
        :param cur_location: current piece location as tuple
        :return: next piece location as tuple
        '''
        # Get all empty pieces around and return none if no pieces around
        pieces_around = self.board.get_pieces_around(cur_location)
        if len(pieces_around) == 0:
            return None

        # Find the piece with maximum empty pieces around
        number_of_pieces_around_them = []
        for piece in pieces_around:
            number_of_pieces_around_them.append(self.board.number_of_empty_pieces_around(piece))
        return pieces_around[HF.index_of_minimum_nonzero(number_of_pieces_around_them)]

    ##################################################################
    # Helping                                                        #
    ##################################################################

    def take_valid_direction(self, matches, directions):
        '''
        After hungarian match piece at each direction, take only the directions which need to be connected
            (i.e. don't match a piece above a top border's piece)
        :param matches: tuples of piece and direction
        :param directions: valid direction
        :return: 
        '''
        return [(piece, direction) for (piece, direction) in matches if direction in directions]
