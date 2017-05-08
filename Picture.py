import numpy as np
from PIL import Image
import Piece
import math
import HelpingFunction as HF
from Constants import *
import DistanceAnalysis as Dist
import Solver


class Picture:
    '''
    img_arr - nparray
    board - nparray of arranged pieces
    pieces - list of pieces (Attention - not nparray)
    height, width - in pixels
    piece_height, piece_width - in pixels
    n, m - width and height (in # of pieces)
    solver - Solver object
    name - title of the picture
    '''

    # TODO rotate pieces?
    # Constructor

    def __init__(self, image_address, n, m=0):
        '''
        Constructor
        :param: board numpy arr[n*n] of Pieces - the board 
        :return: 
        '''
        if m == 0:
            m = n
        # Initialize values
        self.n = n
        self.m = m
        self.name = image_address.split('.jpg')[0]
        img = Image.open(image_address).convert(GRAY)
        self.piece_height = int(math.ceil(img.size[1] / m))
        self.piece_width = int(math.ceil(img.size[0] / n))
        self.height = self.piece_height * m
        self.width = self.piece_width * n
        # Crop the image a little (so all pieces have the same size)
        img = img.crop((0, 0, self.width, self.height))

        # image to array
        self.img_arr = np.array(img)

        # Initialize board and pieces
        self.pieces = self.crop_image()

    def crop_image(self):
        '''
        Crop the image and save the pieces in a list
        :return: list of pieces objects
        '''
        pieces = []
        for i in range(0, self.height, self.piece_height):
            for j in range(0, self.width, self.piece_width):
                pieces.append(Piece.Piece(self.img_arr[i:i+self.piece_height, j:j+self.piece_width].copy(), i*self.width + j))
        return pieces

    # Image handling

    def show_image(self):
        '''
        Print the original image
        :return: 
        '''
        HF.show_image(self.img_arr)