import Board
import numpy as np
import HelpingFunction as HF

board = Board.Board(np.array([[1, None, None], [4, 5, 6], [None, 8, None]]))

########################################################################
# Solver
########################################################################


def get_next_piece_to_match(cur_piece):
    '''
    Get index for the next piece to match, as tuple.
    The next piece is an empty piece around the current piece with maximum empty neightbours
    :param cur_piece: current piece as tuple
    :return: next piece as tuple
    '''
    # Get all empty pieces around and return none if no pieces around
    empty_pieces_around = board.get_empty_pieces_around(cur_piece)
    if empty_pieces_around is []:
        return None
    # Find the piece with maximum empty pieces around
    number_of_pieces_around_them = []
    for piece in empty_pieces_around:
        number_of_pieces_around_them.append(board.number_of_empty_pieces_around(piece))
    return empty_pieces_around[HF.index_of_minimum_nonzero(number_of_pieces_around_them)]
