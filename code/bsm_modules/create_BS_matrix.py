"""



Requirements: math, numpy

"""

import math
import numpy as np

def create_BS_matrix(M, k, r, theta):
    if M < 3:
        return "There must be at least 3 intervals", None, None
    else:
        # Create matrix in CSR form:
        val = []
        col = []
        rowStart = [1]

        for n in range(1, 3 * (M-2) + 5):
            # 1 through 8
            row = math.floor(n / 3) + 1
            if n % 3 == 1:
                value = 1 + (k * r) + k * ((theta) ** 2) * ((row) ** 2)
                column = row
            elif n % 3 == 2:
                value = ((-1 * row * k)/2) * (row * (theta ** 2) + r)
                column = row + 1
            else:
                value = ((-1 * row * k)/2) * (row * (theta ** 2) - r)
                column = row - 1
                rowStart.append(n)
            val.append(value)
            col.append(column)

        rowStart.append(3 * (M-2) + 5)

        val = np.array(val)
        col = np.array(col) - 1
        rowStart = np.array(rowStart) - 1

        return val, col, rowStart