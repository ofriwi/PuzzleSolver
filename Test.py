import numpy as np
from hungarian import *
import Board
from PIL import Image
from Constants import *

board = Board.Board("pic.jpg", 3)
Image.fromarray(board.img_arr, GRAY).show()
Image.fromarray(board._pieces[0].matrix, GRAY).show()

'''
arr = np.array([[[0, 1], [7, 3]], [[-1, -8], [2, 10]]]);
hungarian = Hungarian(arr)
hungarian.calculate()
print(hungarian.get_results())
'''
