import numpy as np
from hungarian import *

arr = np.array([[[0, 1], [7, 3]], [[-1, -8], [2, 10]]]);
hungarian = Hungarian(arr)
hungarian.calculate()
print(hungarian.get_results())