import numpy as np
from hungarian import *
import Board
from PIL import Image
from Constants import *

board = Board.Board(Picture.Picture("pic.jpg", n))
Image.fromarray(board.img_arr).rgb2gray().show()
# Image.fromarray(board._pieces[0].matrix, GRAY).show()

# test_mat = np.zeros((3, 5, 3))
# for i in range(3):
#    for j in range(5):
#        for k in range(3):
#            test_mat[(i, j, k)] = i * 100 + j * 10 + k
# list = [test_mat[i, i ** 2, :] for i in range(3)]
# print(list)




'''
arr = np.array([[[0, 1], [7, 3]], [[-1, -8], [2, 10]]]);
hungarian = Hungarian(arr)
hungarian.calculate()
print(hungarian.get_results())
'''
