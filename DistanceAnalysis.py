import os.path
import numpy as np
from Constants import *
import math


def get_distance_matrix(piece_list, name=''):
    '''
    :param piece_list: a list of pieces
    :return: an lXl matrix of tuples represnting piece distances, where l is piece_list's length
    '''
    # TODO load
    l = len(piece_list)
    file_name = name + str(l) + '.npy'
    if os.path.isfile(file_name):
        distance_matrix = load_from_file(file_name)
    else:
        distance_matrix = np.zeros((l, l), tuple)
        for i in range(l):
            for j in range(l):
                if i == j:
                    distance_matrix[i, j] = (INF, INF, INF, INF)
                else:
                    distance_matrix[i, j] = get_distance_tuple(piece_list[i], piece_list[j])
                print(i.__str__() + ' ' + l.__str__())
        if file_name is not '':
            save_to_file(file_name, distance_matrix)
    return distance_matrix


def get_distance_tuple(piece1, piece2):
    '''
    :param piece1: one piece
    :param piece2: another piece
    :return: a tuple containing all 4 distances
    '''
    tup = ()
    for i in range(4):
        tup += (get_border_distance(piece1.borders[i], piece2.borders[corresponding_side(i)]),)
    return tup
    #return (get_distance_between_borders(piece1, piece2, index) for index in range(4))


def get_border_distance(border1, border2):
    '''
    # Get distance between two matrices.
    :param: One border of a piece as array
    :param: Another border of a piece as array
    :return: Least cost
    '''
    n = len(border1)
    w = int(n * LENGTH_CHECK_PRECENTAGE / 100)
    DT = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i - w + 1 <= j <= i + w - 1:
                DT[i, j] = calculate_dist(abs(border1[i] - border2[j]) + min(DT[i - 1, j],
                                                                    DT[i, j - 1],
                                                                    DT[i - 1, j - 1]))
            else:
                DT[i, j] = INF
        #print(i.__str__() + '/' + n.__str__())
    return DT[n - 1, n - 1]


def corresponding_side(side_index):
    '''
    :param side_index: an integer representing a matrix side
    :return: index representing the other side of the matrix
    '''
    return INVERSE_CONST - side_index


def calculate_dist(pixel_distance):
    '''
    Calculate pixel's distance.
    Currently average, but could be changed.
    (W, B) or (R, G, B) to number
    :param pixel_distance: a tuple representaion of distance between pixels
    :return: the distance
    '''
    return float(sum(pixel_distance)) / max(len(pixel_distance), 1)

# File io


def save_to_file(file, arr):
    np.save(file, arr)


def load_from_file(file):
    return np.load(file)
