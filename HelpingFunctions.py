import numpy as np
from Constants import *

# Get distance between two matrices.
# param 1: One border of a piece as array
# param 2: Another border of a piece as array
# param 3: Width for distance calculation
# return: Least cost
def get_distance(border1, border2, w):
    n = len(border1)
    DT = np.zeros((n, n), float)
    for i in range(0, n):
        for j in range(0, n):
            if i-w+1 <= j <= i+w-1:
                DT[i, j] = abs(border1[i] - border2[j]) + min(DT[i-1, j], DT[i, j-1], DT[i-1, j-1])
            else:
                DT[i, j] = INF
    return DT[n-1, n-1]

print(get_distance([1, 2],[2, 2], 1))
