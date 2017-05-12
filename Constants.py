import math

# Game variables - Change the functionallity of the game, should be changed

IMG_ADR = "lily.jpg"
N = 3
LENGTH_CHECK_PRECENTAGE = 10
MATCH_NUM = 3  # 10
SUBFOLDER = "picture_data/"

DEBUG = False  # True
STEP_BY_STEP_DEBUG = False  # True

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

# Result Indexes
RUNNING_TIME = 0
CORRECT_BORDERS = 1
IS_TRUE = 2
COST = 3
SOLUTION = 4

TUPLE_RESULT_INDEXES = [RUNNING_TIME, CORRECT_BORDERS, IS_TRUE, COST]
PARAMETER_NAME = ["Running Time", "Correct Borders", "Is Correct Solution", "Cost"]

# image lis
IMAGE_LIST = ["Lenna", "LennaAllEffects", "MonetLilies", "RepeatingText"]
