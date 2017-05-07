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


def show_image(img_arr):
    Image.fromarray(img_arr, GRAY).show()
