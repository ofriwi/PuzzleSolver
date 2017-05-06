import DistanceAnalysis as Dist

'''
Piece class represents a single Puzzle piece
Attributes:
1) boolean isLegal - Legal Piece or a representation of an empty piece
2) 2D list matrix - representing the picture
3) 2D borders - a list that contains 4 lists, each of which represents a 
   different border, according to the order defined earlier.
'''


class Piece:
    def __init__(self, matrix):
        '''
        Construct a legal Piece
        :param matrix is a square matrix representing the puzzle piece
        :param n is matrix's side length
         '''
        self.n = len(matrix)
        self.matrix = matrix
        top_line = self.matrix[0]
        bottom_line = self.matrix[self.n - 1]
        left_col = [row[0] for row in matrix]
        right_col = [row[self.n - 1] for row in matrix]
        self.borders = [top_line, left_col, right_col, bottom_line]

    def get_side(self, side_index):
        '''
        :param side_index: an integer representing a matrix side
        :return: corresponding side
        '''
        return self.borders[side_index]

    def get_piece_distance(self, other, side_index):
        '''
        :param other: another piece
        :param side_index: side index to be compared
        :return: distance between corresponding sides given
        '''
        return Dist.get_distance(self.borders[side_index], other.borders[
            Dist.corresponding_side(side_index)])

    def get_piece_distance_tuple(self, other):
        '''
        :param other: another piece
        :return: a tuple containing all 4 distances
        '''
        return (self.get_piece_distance(other, index) for index in range(4))
