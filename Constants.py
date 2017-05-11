import math

# Game variables - Change the functionallity of the game, should be changed

IMG_ADR = "lily.jpg"
N = 5
LENGTH_CHECK_PRECENTAGE = 10
MATCH_NUM = 5#10
SUBFOLDER = "picture_data/"

DEBUG = True
STEP_BY_STEP_DEBUG = False#True

# System variables - Should not be changed after done developing

INF = 2147483647  # float('inf') - 1
GRAY = 'L'
PIXEL_DIMENTION = 2

# Side indexes
TOP = 0  # (i-1,j)
LEFT = 1  # (i,j-1)
RIGHT = 2  # (i, j+1)
BOTTOM = 3  # (i+1, j)
INVERSE = 3
NO_PIECE = -1
ALL_DIRECTIONS = [TOP, LEFT, RIGHT, BOTTOM]
