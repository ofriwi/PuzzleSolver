from PIL import Image
import numpy as np
# import scipy.misc
import os

from Constants import *
import numpy as np


def index_of_minimum(arr):
    return arr.index(min(arr))


def index_of_minimum_nonzero(arr):
    return arr.index(min(x for x in arr if x > 0))


def index_of_maximum(arr):
    return arr.index(max(arr))


def index_of_maximum_not_inf(arr):
    return arr.index(max(x for x in arr if x < INF))


def show_image(img_arr):
    Image.fromarray(img_arr, GRAY).show()


def tuple_list_to_2d(lst):
    return np.array([lst[i, :] for i in range(len(lst))])


def matrix_to_picture(piece_matrix, picture_name):
    '''
    :param piece_matrix: a matrix of pieces to be converted into a picture 
    :param picture_name: a name for the picture to be saved
    '''
    piece_length = piece_matrix[0][0].get_length()
    n = piece_length * len(piece_matrix)
    picture_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            piece = piece_matrix[i // piece_length][j // piece_length]
            picture_matrix[i][j] = piece[i % piece_length][j % piece_length]
    image = Image.fromArray(picture_matrix)
    image.save(picture_name)


def best_k_values(dict, k):
    '''
    :param dict: a dictionary 
    :param k: an integer k
    :return: a list of the smallest k keys in the dictionary
    '''
    key_lst = [key for key in dict.keys()]
    min_lst = []
    for i in range(min(k, len(key_lst))):
        minimal = min(key_lst)
        min_lst.append(minimal)
        key_lst.remove(minimal)
    return min_lst


def address_to_name(address):
    '''
    :param address: a file address 
    :return: file name
    '''
    return (os.path.splitext(address)[0])
