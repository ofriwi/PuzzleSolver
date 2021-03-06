import time

import Board
import HelpingFunction as HF
import hungarian as Hungarian
import Constants as const
import numpy as np
from Constants import *
import itertools


class Solver:
    '''
    picture - Picture object
    board - Board object
    current_cost - cost of the current preposed solution
    '''

    # Constructor
    def __init__(self, picture, solver_type):
        self._picture = picture
        self.board = Board.Board(picture)
        self.current_cost = 0
        self.solver_type = solver_type
        if not STEP_BY_STEP_DEBUG:
            self.results = self.solve()

    def get_results(self):
        return self.results

    # Solver

    def solve(self):
        time_before = time.time()
        if self.solver_type == BETTER or self.solver_type == OLD_HUNGARIAN or self.solver_type == GREEDY2:
            matches = self.our_algorithm()
        elif self.solver_type == BRUTE_FORCE:
            matches = self.brute_force_algorithm()
        elif self.solver_type == INTUITIVE:
            matches = self.intuitive_algorithm()
        else:
            matches = None

        best_matches, costs = self.get_best_matches(matches, MATCH_NUM)
        best_match = best_matches[0]
        best_match_array = best_matches[0].get_solution_array()

        time_after = time.time()
        run_time = time_after - time_before

        correctness = best_match.get_correctness()
        is_correct = (correctness == 100)

        result_tuple = run_time, correctness, is_correct, costs[0], best_match_array
        return result_tuple

    def brute_force_algorithm(self):
        matches = {}
        permutations = itertools.permutations(range(len(self._picture.pieces)))
        for indexes in permutations:
            self.board = Board.Board(self._picture)
            indexes = list(indexes)
            for k in range(self.board.n):
                for l in range(self.board.m):
                    self.board.add_piece_index_in_position((k, l), indexes[0])
                    indexes.pop(0)
            matches[self.board.get_total_cost()] = self.board
        return matches

    def intuitive_algorithm(self):
        matches = {}
        D = self.board.get_distance_matrix()
        last_cell = 0
        upper_cell = 0
        for index in range(len(self._picture.pieces)):
            self.board = Board.Board(self._picture)
            cost = 0
            for k in range(self.board.n):
                for l in range(self.board.m):
                    if k == 0 and l == 0:
                        match_index = index
                        upper_cell = index
                    elif l != 0:
                        match_index = np.argmin(D[last_cell, self.board.get_unassigned_cells(), RIGHT])
                        match_index = self.board.get_unassigned_cells()[match_index]
                        cost += D[last_cell, match_index, RIGHT]
                    else:
                        match_index = np.argmin(D[upper_cell, self.board.get_unassigned_cells(), BOTTOM])
                        match_index = self.board.get_unassigned_cells()[match_index]
                        cost += D[last_cell, match_index, BOTTOM]
                        upper_cell = match_index
                    self.board.add_piece_index_in_position((k, l), match_index)
                    last_cell = match_index
            matches[cost] = self.board
        return matches

    def our_algorithm(self):
        '''
        Run our algorithm
        :param solver_type: 
        :return: 
        '''
        matches = {}
        if self.board.n > 2 and self.board.m > 2:
            starting = 1
        else:
            starting = 0
        for k in range(starting, self.board.n - starting):
            for l in range(starting, self.board.m - starting):
                for index in range(self.board.n * self.board.m):
                    (cost, board) = self.single_solution((k, l), index)
                    matches[cost] = board
                print(str(l) + " checks out of " + str(self.board.m - 2 * starting))
            print(str(k) + " large iter out of " + str(self.board.n - 2 * starting))
        return matches

    def get_best_matches(self, matches, number_of_values):
        '''
        Get n best values in matches dictonery
        :param matches: 
        :param number_of_values: 
        :return: best values as (cost, board)
        '''
        costs = HF.best_k_values(matches, number_of_values)
        best_matches = []
        for key in costs:
            best_matches.append(matches[key])
            if SHOW_SOL:
                matches[key].show_solution()
            if DEBUG:
                print(key)
        return best_matches, costs

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

        # self.board.show_solution()

        return self.current_cost, self.board

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
        if self.solver_type == BETTER:
            assign, cost = self.better_hungarian(piece_index, empty_directions,
                                                 pos)
        elif self.solver_type == OLD_HUNGARIAN:
            assign, cost = self.get_hungarian(piece_index, empty_directions)
        elif self.solver_type == GREEDY2:
            assigns = []
            costs = []
            for direction in empty_directions:
                assigns.append(np.argmin(self.board.get_distance_matrix()[piece_index, self.board.get_unassigned_cells(), direction]))
                ix = empty_directions.index(direction)
                assigns[ix] = self.board.get_unassigned_cells()[assigns[ix]]
                costs.append(self.board.get_distance_matrix()[piece_index, assigns[ix], direction])

            cost = min(costs)
            index = costs.index(cost)
            assign = [(assigns[index], empty_directions[index])]
        else:
            assign = 0
            cost = 0
        self.current_cost += cost

        # Lines 10 - 11
        for (piece_index, direction) in assign:
            self.board.add_piece_index_in_direction(pos, piece_index,
                                                    direction)

        if STEP_BY_STEP_DEBUG:
            self.board.show_solution()
            if SLEEP == -1:
                input()
            elif not SLEEP == 0:
                time.sleep(SLEEP)

        if not self.board.is_puzzle_completed():
            next_pos = self.get_next_position_to_match(pos)
            while next_pos is not None:
                self.build_around(next_pos)
                next_pos = self.get_next_position_to_match(pos)

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
        row_distance_matrix = self.board.get_distance_matrix()[
            piece_index, self.board.get_unassigned_cells()]
        # print(row_distance_matrix)
        row_distance_matrix = row_distance_matrix[:, valid_directions]
        # print(row_distance_matrix)
        # Convert to 2d array
        H = HF.tuple_list_to_2d(row_distance_matrix)
        # Take only valid directions
        # H = H[:, valid_directions]
        # Calculate hungarian
        hungarian = Hungarian.Hungarian(H)
        hungarian.calculate()
        # Get the correct indexes of unassigned cells and vald directions
        result = [(self.board.get_unassigned_cells()[index],
                   valid_directions[direction]) for (index, direction) in
                  hungarian.get_results()]
        cost = hungarian.get_total_potential()
        return result, cost

    def better_hungarian(self, piece_index, valid_directions, pos):
        '''
        Get the hungarian arrangement around a piece
        :param piece_index: the piece's index
        :param valid_directions: direction with empty cells as list [T, R, L, B]
        :return: list of tuples (index, direction) where index is the index of the matching piece 
            and the direction is the direction relative to the piece
        '''
        # Get i * unassigned
        D = self.board.get_distance_matrix()
        # row_distance_matrix = get_row
        # print(row_distance_matrix)
        # Convert to 2d array
        H = self.get_H_matrix(
            pos)  # row_distance_matrix#.reshape(row_distance_matrix.shape[1], row_distance_matrix.shape[2])
        # Take only valid directions
        H = H[:, valid_directions]
        # Calculate hungarian
        hungarian = Hungarian.Hungarian(H)
        hungarian.calculate()
        # Get the correct indexes of unassigned cells and valid directions
        result = [(self.board.get_unassigned_cells()[index],
                   valid_directions[direction]) for (index, direction) in
                  hungarian.get_results()]
        cost = hungarian.get_total_potential()
        return result, cost

    def get_H_matrix(self, pos):
        H = np.ones((len(self.board.get_unassigned_cells()), 4)) * INF
        for direction in self.board.get_empty_directions_around(pos):
            empty_cell_pos = self.board.get_position_in_direction(pos,
                                                                  direction)
            H[:, direction] = self.row_matrix_for_pos(empty_cell_pos)
        return H

    def row_matrix_for_pos(self, pos):
        D = self.board.get_distance_matrix()
        D = D[:, self.board.get_unassigned_cells(), :]
        avg = 0
        counter = 0
        for direction in ALL_DIRECTIONS:
            other_piece_pos = self.board.get_position_in_direction(pos,
                                                                   direction)
            if self.board.is_cell_filled(other_piece_pos):
                other_piece = self.board.get_piece_index_in_position(
                    other_piece_pos)
                row_around = D[
                             other_piece, 0:len(self.board.get_unassigned_cells())
                ,
                             INVERSE - direction]
                avg += row_around
                counter += 1
        avg = avg / counter
        return avg

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
            number_of_pieces_around_them.append(
                self.board.number_of_empty_pieces_around(piece))
        if max(number_of_pieces_around_them) == 0:
            return None
        return pieces_around[HF.index_of_maximum(number_of_pieces_around_them)]
