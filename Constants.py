import math

# Game variables - Change the functionallity of the game, should be changed

IMG_ADR = "etsi.jpg"
N = 4
LENGTH_CHECK_PRECENTAGE = 10
MATCH_NUM = 3
SUBFOLDER = "picture_data/"

DEBUG = False#True
STEP_BY_STEP_DEBUG = False#True
SHOW_SOL = True
IMAGE_LIST = ["etsi.jpg", "face.jpg"]
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

# Algorithms
BETTER = 0
OLD_HUNGARIAN = 1
BRUTE_FORCE = 2
INTUITIVE = 3
ALGO_NAME = ['BETTER', 'old hungarian', 'brute force', 'greedy']
