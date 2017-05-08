import Board
import DistanceAnalysis as Dist
import HelpingFunction as HF
import hungarian as Hungarian
from Constants import *
import numpy as np


class Solver:
    '''
    board - Board object
    D - distances matrix
    '''

    # Main solver
    def solve(self):
        # TODO
        return

    # Constructor
    def __init__(self, picture):
        self.board = Board.Board(picture)
        self.D = self.board.get_distance_matrix()

    # Lines 8-9
    def get_hungarian(self, piece_index, valid_directions):
        '''
        Get the hungarian arrangement around a piece
        :param piece_index: the piece's index
        :return: list of tuples (index, position) where index is the index of the matching piece 
            and the position is the position relative to the piece
        '''
        H = HF.tuple_list_to_2d(self.D[piece_index, :])
        hungarian = Hungarian.Hungarian(H)
        hungarian.calculate()
        return self.take_valid_direction(hungarian.get_results(), valid_directions)

    # Line 13
    def get_next_location_to_match(self, cur_location):
        '''
        Get index for the next piece to match, as tuple.
        The next piece is an empty piece around the current piece with maximum empty neightbours
        :param cur_location: current piece location as tuple
        :return: next piece location as tuple
        '''
        # Get all empty pieces around and return none if no pieces around
        empty_pieces_around = self.board.get_empty_pieces_around(cur_location)
        if empty_pieces_around is []:
            return None

        # Find the piece with maximum empty pieces around
        number_of_pieces_around_them = []
        for piece in empty_pieces_around:
            number_of_pieces_around_them.append(self.board.number_of_empty_pieces_around(piece))
        return empty_pieces_around[HF.index_of_minimum_nonzero(number_of_pieces_around_them)]

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
        return [(piece, direction) for (piece, direction) in matches if directions.contains(direction)]
