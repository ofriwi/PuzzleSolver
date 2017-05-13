from PIL import Image

import Board
import numpy as np
import HelpingFunction as HF
import Solver
from Constants import *
import DistanceAnalysis as Dist
import Picture
import os
import time
#import scipy.misc


def single_solver_type_comparison(image_address, solver_type, min_n, max_n=0):
    '''
    :param image_address: adress of desired image 
    param min_n: min_n^2 is the minimal number of puzzle_pieces to be cut
    :param max_n: max_n^2 is the maximal number of puzzle pieces to be cut
    '''
    if (max_n == 0):  # only once
        max_n = min_n
    result_dictionary = dict()
    #for n in range(min_n, max_n + 1):
     #   single_run(image_address, n, result_file, solver_type, result_dictionary)

    # writing results
    picture_name = HF.address_to_name(image_address)
    result_file = open(SUBFOLDER + HF.address_to_name(image_address), "w")
    result_file.write(picture_name + " - " + ALGO_NAME[solver_type] + "\n")
    #for result_param in TUPLE_RESLT_INDEXES:
     #   result_file.write(PARAMETER_NAME[result_param] + "\n")
      #  for n in range(min_n, max_n + 1):
       #     result_file.write(result_dictionary(n, solver_type)[i])
            # TODO insert PARAMETER_NAME and result_param indexes to CONSTANTS


def single_run(image_address, n, solver_type, result_dictionary):
    '''
    :param image_address: address of desired image 
    :param n: n^2 is the number of puzzle pieces to be cut
    '''
    square_puzzle = Picture.Picture(image_address, n, n)
    picture_name = HF.address_to_name(image_address)
    solution_name = (picture_name + " - " + str(n) + "X" + str(n) + " pieces - " + ALGO_NAME[solver_type])
    solver = Solver.Solver(square_puzzle, solver_type)
    result_dictionary[(n, solver_type)] = solver.get_results
    # scipy.misc.imsave(solution_name + "jpg", solver.get_results[5])


def create_square_puzzle(image_address, n):
    return Picture.Picture(image_address, n, n)


# run main
# single_pic_sol(IMG_ADR, N)


picture = create_square_puzzle(IMG_ADR, N)
solver = Solver.Solver(picture, BETTER)
r = solver.get_results()
if STEP_BY_STEP_DEBUG:
    solver.single_solution((1, 1), 5)
picture.picture_cost()
# picture = create_square_puzzle(IMG_ADR, 5)
# solver = Solver.Solver(picture)
# picture = create_square_puzzle(IMG_ADR, 6)
# solver = Solver.Solver(picture)

# print(solver.get_hungarian(0, [RIGHT, BOTTOM]))

# Dist.get_distance_between_borders(board.pieces[0], board.pieces[1], 0)
# print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[2].get_side(LEFT)))
# print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[1].get_side(LEFT)))
# print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[1].get_side(TOP)))
# print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[2].get_side(TOP)))
# board.show_image()
# print(Dist.get_distance_matrix(picture.pieces))
# for p in board.pieces:
#   p.show()
# board.print_image()
# board.pieces[0].show()
# board.board[0, 0] = board.pieces[1]
# board.board[0, 1] = board.pieces[0]
# board.board[1, 0] = board.pieces[0]
# board.board[1, 1] = board.pieces[0]
# board.print_solution()
# board.get_solution()
