import math

# Game variables - Change the functionallity of the game, should be changed

IMG_ADR = "LennaAllEffects.jpg"
N = 10
LENGTH_CHECK_PRECENTAGE = 10
MATCH_NUM = 3
SUBFOLDER = "testPictures/"

DEBUG = False  # True

#STEP_BY_STEP_DEBUG = True
#K_STEP = 3
#L_STEP = 3
#PIECE_INDEX_STEP = 30
#SLEEP = 0  # positive time, 0 for no sleep, -1 for input()
STEP_BY_STEP_DEBUG = False

# SHOW_SOL = True
SHOW_SOL = False

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
INTUITIVE = 2
BRUTE_FORCE = 3
OUR_FROM_MIDDLE = 4
GREEDY2 = 5
ALGO_INDEX = [BETTER, OLD_HUNGARIAN, INTUITIVE]
ALGO_NAME = ['BETTER', 'old hungarian', 'greedy', 'brute force', 'our from middle', 'greedy2']

# Results
RUNNING_TIME = 0
CORRECT_BORDERS = 1
IS_CORRECT = 2
COST = 3
SOLUTION = 4

TUPLE_RESULT_INDEXES = [RUNNING_TIME, CORRECT_BORDERS, IS_CORRECT, COST]
PARAMETER_NAME = ["Running Time", "Correct Borders", "Is Correct", "Cost"]
