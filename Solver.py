import Board
import HelpingFunction as HF
import hungarian as Hungarian


class Solver:
    '''
    picture - Picture object
    board - Board object
    current_cost - cost of the current preposed solution
    '''

    # Constructor
    def __init__(self, picture):
        self._picture = picture
        self.board = Board.Board(picture)
        self.current_cost = 0
        self.solve()

    # Solver

    def solve(self):
        self.matches = {}
        if self.board.n > 2 and self.board.m > 2:
            STARTING = 1
        else:
            STARTING = 0 #TODO: change
        for k in range(STARTING, self.board.n - STARTING):
            for l in range(STARTING, self.board.m - STARTING):
                for index in range(self.board.n * self.board.m):
                    (cost, board) = self.single_solution((k, l), index)
                    self.matches[cost] = board
        min_cost = min(self.matches.keys())
        self.matches[min_cost].show_solution()


    def single_solution(self, pos, piece_index):
        '''
        Try a single solution
        :param pos: the position to build around
        :param piece_index: the index of the piece in the position
        :return: 
        '''

        # init
        self.board = Board.Board(self._picture)
        self.current_cost = 0

        # Lines 5 - 7
        self.board.add_piece_index_in_position(pos, piece_index)

        self.build_around(pos)

        # TODO : save cost

        #self.board.show_solution()
        #input()
        return self.current_cost, self.board # TODO: better

    def build_around(self, pos):
        '''
        Build the 4 pieces around a piece.
        :param pos: the position to build around
        :param piece_index: the index of the piece in the position
        :return: 
        '''
        piece_index = self.board.get_piece_index_in_position(pos)

        # Lines 8 - 9
        empty_directions = self.board.get_empty_directions_around(pos)
        assign, cost = self.get_hungarian(piece_index, empty_directions)
        self.current_cost += cost

        # Lines 10 - 11
        for (piece_index, direction) in assign:
            self.board.add_piece_index_in_direction(pos, piece_index, direction)

        if not self.board.is_puzzle_completed():
            next_pos = self.get_next_position_to_match(pos)
            while next_pos is not None:
                self.build_around(next_pos)
                next_pos = self.get_next_position_to_match(pos) # TODO check if better solution

    # Lines 8-9
    def get_hungarian(self, piece_index, valid_directions):
        '''
        Get the hungarian arrangement around a piece
        :param piece_index: the piece's index
        :param valid_directions: direction with empty cells as list [T, R, L, B]
        :return: list of tuples (index, direction) where index is the index of the matching piece 
            and the direction is the direction relative to the piece
        '''
        # Get i * unassigned
        row_distance_matrix = self.board.get_distance_matrix()[piece_index, self.board.get_unassigned_cells()]
        # Convert to 2d array
        H = HF.tuple_list_to_2d(row_distance_matrix)
        # Take only valid directions
        H = H[:, valid_directions]
        # Calculate hungarian
        hungarian = Hungarian.Hungarian(H)
        hungarian.calculate()
        # Get the correct indexes of unassigned cells and vald directions
        result =[(self.board.get_unassigned_cells()[index], valid_directions[direction]) for (index, direction) in hungarian.get_results()]
        cost = hungarian.get_total_potential()
        return result, cost

    # Line 13
    def get_next_position_to_match(self, cur_pos):
        '''
        Get position for the next piece to match, as tuple.
        The next piece is a piece around the current piece with maximum empty neighbours
        :param cur_pos: current piece position as tuple
        :return: next piece location as tuple
        '''
        # Get all pieces around and return none if no pieces around
        pieces_around = self.board.get_positions_around(cur_pos)

        # Find the piece with maximum empty pieces around
        number_of_pieces_around_them = []
        for piece in pieces_around:
            number_of_pieces_around_them.append(self.board.number_of_empty_pieces_around(piece))
        if max(number_of_pieces_around_them) == 0:
            return None
        return pieces_around[HF.index_of_maximum(number_of_pieces_around_them)]
