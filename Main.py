import Board
import numpy as np
import HelpingFunction as HF
import Solver
from Constants import *
import DistanceAnalysis as Dist
import Picture


def create_square_puzzle(image_address, n):
    return Picture.Picture(image_address, n, n)

picture = create_square_puzzle(IMG_ADR, N)
solver = Solver.Solver(picture)
print(solver.get_hungarian(0))


#Dist.get_distance_between_borders(board.pieces[0], board.pieces[1], 0)
#print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[2].get_side(LEFT)))
#print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[1].get_side(LEFT)))
#print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[1].get_side(TOP)))
#print(Dist.get_distance(board.pieces[0].get_side(RIGHT), board.pieces[2].get_side(TOP)))
#board.show_image()
#print(Dist.get_distance_matrix(picture.pieces))
#for p in board.pieces:
 #   p.show()
#board.print_image()
#board.pieces[0].show()
#board.board[0, 0] = board.pieces[1]
#board.board[0, 1] = board.pieces[0]
#board.board[1, 0] = board.pieces[0]
#board.board[1, 1] = board.pieces[0]
#board.print_solution()
#board.get_solution()
print()