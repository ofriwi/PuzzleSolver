'''
Indexes representing matrix's sides.
'''
TOP = 0;
LEFT = 1;
BOTTOM = 2;
RIGHT = 3

def corresponding_side(side_index):
    '''
    :param side_index: an integer representing a matrix side
    :return: index representing the other side of the matrix
    '''
    return (side_index + 2) % 4


'''
Piece class represents a single Puzzle piece
Attributes:
1) boolean isLegal - Legal Piece or a representation of an empty piece
2) 2D list matrix - representing the picture
3) 2D borders - a list that contains 4 lists, each of which represents a 
   different border, according to the order defined earlier.
'''
class Piece:

    '''
    Construct a legal Piece
    :param matrix is a square matrix representing the puzzle piece
    :param n is matrix's side length
    '''

    def __init__(self, matrix, n, is_legal = True):
        self.is_legal = is_legal
        self.n = n
        if is_legal:
            self.matrix = matrix
            top_line = self.matrix[0]
            bottom_line = self.matrix[n - 1]
            left_col = [row[0] for row in matrix]
            right_col = [row[n-1] for  row in matrix]
            self.borders = [top_line, left_col, bottom_line, right_col]

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
        distance = 0
        for i in range(self.n):
           distance += (self.borders[side_index]-
                        self.borders[corresponding_side(side_index)])**2
        return distance

    def get_piece_distance_tuple(self, other):
        '''
        :param other: another piece
        :return: a tuple containing all 4 distances
        '''
        return (self.get_piece_distance(other, index) for index in range(4))


