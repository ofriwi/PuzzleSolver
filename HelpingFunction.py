from PIL import Image

from Constants import *
import numpy as np


def index_of_minimum(arr):
    return arr.index(min(arr))


def index_of_minimum_nonzero(arr):
    return arr.index(min(arr) > 0)


def index_of_maximum(arr):
    return arr.index(max(arr))


def index_of_maximum_not_inf(arr):
    return arr.index(max(arr) < INF)


def rgb2gray(rgb, to_gray=True):
    if to_gray:
        r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
        return 0.2989 * r + 0.5870 * g + 0.1140 * b
    else:
        return rgb

def show_image(img_arr):
    Image.fromarray(img_arr, GRAY).show()
