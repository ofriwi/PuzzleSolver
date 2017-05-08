import DistanceAnalysis as Dist
from Constants import *
import HelpingFunction as HF

'''
Piece class represents a single Puzzle piece
Attributes:
1) boolean isLegal - Legal Piece or a representation of an empty piece
2) 2D list matrix - representing the picture
3) 2D borders - a list that contains 4 lists, each of which represents a 
   different border, according to the order defined earlier.
'''


class Piece:
    def __init__(self, matrix, index):
        '''
        Construct a legal Piece
        :param matrix is a square matrix representing the puzzle piece
        :param n is matrix's side length
         '''
        self.n = matrix.shape[0]
        self.m = matrix.shape[1]
        self.matrix = matrix
        self._index = index
        top_line = self.matrix[0, :]
        bottom_line = self.matrix[self.n - 1, :]
        left_col = self.matrix[:, 0]
        right_col = self.matrix[:, self.m - 1]
        self.borders = [top_line, left_col, right_col, bottom_line]

    def get_side(self, side_index):
        '''
        :param side_index: an integer representing a matrix side
        :return: corresponding side
        '''
        return self.borders[side_index]

    def show(self):
        HF.show_image(self.matrix)

    def get_index(self):
        return self._index

    def get_length(self):
        '''
        :return: piece side length 
        '''
        return len(self.borders[0])
