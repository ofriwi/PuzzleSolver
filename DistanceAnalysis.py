import numpy as np
import Piece
from Constants import *


# Get distance between two matrices.
# param 1: One border of a piece as array
# param 2: Another border of a piece as array
# param 3: Width for distance calculation
# return: Least cost


def get_distance(border1, border2):
    n = len(border1)
    w = n * LENGTH_CHECK_PRECENTAGE
    DT = np.zeros((n, n), float)
    for i in range(0, n):
        for j in range(0, n):
            if i - w + 1 <= j <= i + w - 1:
                DT[i, j] = abs(border1[i] - border2[j]) + min(DT[i - 1, j],
                                                              DT[i, j - 1],
                                                              DT[i - 1, j - 1])
            else:
                DT[i, j] = INF
    return DT[n - 1, n - 1]


def corresponding_side(side_index):
    '''
    :param side_index: an integer representing a matrix side
    :return: index representing the other side of the matrix
    '''
    return INVERSE_CONST - side_index


def get_distance_matrix(piece_list):
    '''
    :param piece_list: a list of pieces
    :return: an lXl matrix of tuples represnting piece distances, where l is piece_list's length
    '''
    l = len(piece_list)
    distance_matrix = np.zeros((n, n), float)
    for i in range(l):
        for j in range(l):
            distance_matrix[i, j] = piece_list[i].get_distance_tuple(
                piece_list[j])
    return distance_matrix