import numpy as np
from PIL import Image

import DistanceAnalysis as Dist
import HelpingFunction as HF
import Piece
from Constants import *


class Picture:
    '''
    img_arr - np array
    board - np array of arranged pieces
    pieces - list of pieces (Attention - not np array)
    height, width - in pixels
    piece_height, piece_width - in pixels
    n, m - width and height (in # of pieces)
    solver - Solver object
    name - title of the picture
    '''

    # Constructor

    def __init__(self, image_address, n, m=0):
        '''
        Constructor
        :param: board numpy arr[n*n] of Pieces - the board 
        :return: 
        '''
        if m == 0:
            m = n
        image_address = SUBFOLDER + image_address
        # Initialize values
        self.n = n
        self.m = m
        self.name = image_address.split('.jpg')[0]
        img = Image.open(image_address).convert(GRAY)
        self.piece_height = int(math.floor(img.size[1] / m))
        self.piece_width = int(math.floor(img.size[0] / n))
        self.height = self.piece_height * m
        self.width = self.piece_width * n
        # Crop the image a little (so all pieces have the same size)
        img = img.crop((0, 0, self.width, self.height))

        # image to array
        self.img_arr = np.array(img)

        # Initialize board and pieces
        self.pieces = self.crop_image()
        self.distance_matrix = Dist.get_distance_matrix(self.pieces, self.name)

    def crop_image(self):
        '''
        Crop the image and save the pieces in a list
        :return: list of pieces objects
        '''
        pieces = []
        for i in range(0, self.height, self.piece_height):
            for j in range(0, self.width, self.piece_width):
                pieces.append(Piece.Piece(self.img_arr[i:i + self.piece_height,
                                          j:j + self.piece_width].copy()))
        return pieces

    def picture_cost(self):
        total_cost = 0
        for i in range(self.n):
            for j in range(self.m):
                index = i * self.n + j
                if not j == self.m - 1:
                    total_cost += Dist.get_border_distance(self.pieces[index].get_side(
                        RIGHT), self.pieces[index + 1].get_side(
                        LEFT))
                if not i == self.n - 1:
                    total_cost += Dist.get_border_distance(self.pieces[index].get_side(
                        BOTTOM), self.pieces[index + 1].get_side(TOP))
        if DEBUG:
            print('pic_cost = ' + str(total_cost))
        return total_cost
    # Image handling

    def show_image(self):
        '''
        Print the original image
        :return: 
        '''
        HF.show_image(self.img_arr)
