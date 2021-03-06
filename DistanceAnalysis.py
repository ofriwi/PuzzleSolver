import os.path
import numpy as np
from Constants import *
import math


def get_distance_matrix(piece_list, name=''):
    '''
    :param piece_list: a list of pieces
    :return: an lXl matrix containing lists of length 4 representing piece 
    distances, where l is piece_list's length
    '''
    l = len(piece_list)
    file_name = name + str(l) + '.npy'
    if os.path.isfile(file_name):
        distance_matrix = load_from_file(file_name)
    else:
        distance_matrix = np.zeros((l, l, 4), dtype=float)
        # fill matrix
        for i in range(l):
            # mid-run printing
            print(i.__str__() + ' ' + l.__str__())
            for j in range(l):
                distance_list_ij = get_distance_list(piece_list[i],
                                                     piece_list[j])
                if i == j:
                    distance_matrix[i, j, :] = INF
                else:
                    distance_matrix[i, j, :] = distance_list_ij

                    # for k in range(4):
                    #   if i == j:
                    #      distance_matrix[i, j, k] = INF
                    # else:
                    #    distance_matrix[i, j, k] = distance_list_ij[k]

    if file_name is not '':
        save_to_file(file_name, distance_matrix)
    return distance_matrix


def get_distance_list(piece1, piece2):
    '''
    :param piece1: one piece
    :param piece2: another piece
    :return: a tuple containing all 4 distances
    '''
    lst = [get_border_distance(piece1.borders[i],
                               piece2.borders[corresponding_side(i)])
           for i in range(4)]
    return lst
    # return (get_distance_between_borders(piece1, piece2, index) for index in range(4))


def get_border_distance(border1, border2):
    '''
    # Get distance between two matrices.
    :param: One border of a piece as array
    :param: Another border of a piece as array
    :return: Least cost
    '''
    n = len(border1)
    w = int(n * LENGTH_CHECK_PRECENTAGE / 100)
    DT = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i - w + 1 <= j <= i + w - 1:
                DT[i, j] = step_distance(DT, border1, border2, i, j)
            else:
                DT[i, j] = INF
    return DT[n - 1, n - 1]


def step_distance(DT, border1, border2, i, j):
    '''
    Calculate the distance between two pixels, and add the minimum from previous step
    :param DT: Distance matrix
    :param border1: piece1's border
    :param border2: piece2's border
    :param i: i index
    :param j: j index
    :return: calculated distance
    '''
    if i == 0 and j == 0:
        step = abs(int(border1[i]) - int(border2[j]))
    elif i == 0:
        step = abs(int(border1[i]) - int(border2[j])) + DT[i, j - 1]
    elif j == 0:
        step = abs(int(border1[i]) - int(border2[j])) + DT[i - 1, j]
    else:
        step = abs(int(border1[i]) - int(border2[j])) + min(DT[i - 1, j], DT[i, j - 1]
                                                  , DT[i - 1, j - 1])
    return step

def corresponding_side(side_index):
    '''
    :param side_index: an integer representing a matrix side
    :return: index representing the other side of the matrix
    '''
    return INVERSE - side_index


# File io


def save_to_file(file, arr):
    np.save(file, arr)


def load_from_file(file):
    return np.load(file)
