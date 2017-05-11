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


def single_pic_sol(image_address, min_n, max_n=0):
    '''
    :param image_address: adress of desired image 
    param min_n: min_n^2 is the minimal number of puzzle_pieces to be cut
    :param max_n: max_n^2 is the maximal number of puzzle pieces to be cut
    '''
    if (max_n == 0):  # only once
        max_n = min_n
    result_file = open(SUBFOLDER + HF.address_to_name(image_address), "w")
    for n in range(min_n, max_n):
        single_run(image_address, n, result_file)


def single_run(image_address, n, result_file):
    '''
    :param image_address: address of desired image 
    :param n: n^2 is the number of puzzle pieces to be cut
    '''
    square_puzzle = Picture.Picture(image_address, n, n)
    picture_name = HF.address_to_name((image_address))
    solution_name = (picture_name + " - " + str(n) + "X" + str(n) + " pieces")
    time_before = time.time()
    puzzle_solver = Solver(square_puzzle)
    piece_board = puzzle_solver.solve()
    piece_matrix = piece_board.get_solution_array()
    running_time = time.time - time_before()
    HF.matrix_to_picture(piece_matrix, solution_name)
    result_file.write(
        "%X% pieces: % [sec]\n" % str(n) % str(n) % str(running_time))


def create_square_puzzle(image_address, n):
    return Picture.Picture(image_address, n, n)


# run main
# single_pic_sol(IMG_ADR, N)


picture = create_square_puzzle(IMG_ADR, N)
solver = Solver.Solver(picture)
if STEP_BY_STEP_DEBUG:
    solver.single_solution((1, 1), 5)
picture.picture_cost()
#picture = create_square_puzzle(IMG_ADR, 5)
#solver = Solver.Solver(picture)
#picture = create_square_puzzle(IMG_ADR, 6)
#solver = Solver.Solver(picture)

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
