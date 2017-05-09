import math

# Game variables - Change the functionallity of the game, should be changed

IMG_ADR = "etsi.jpg"
N = 10
LENGTH_CHECK_PRECENTAGE = 10

# System variables - Should not be changed after done developing

INF = 2147483647  # float('inf') - 1
GRAY = 'LA'
PIXEL_DIMENTION = 2

# Side indexes
TOP = 0  # (i-1,j)
LEFT = 1  # (i,j-1)
RIGHT = 2  # (i, j+1)
BOTTOM = 3  # (i+1, j)
INVERSE_CONST = 3
NO_PIECE = -1
