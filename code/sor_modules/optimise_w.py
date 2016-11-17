"""

optimise_w.py

This module contains 1 function, op_w() which takes 2 arguments:
  - list - A list of error reductions for previous iterations, floats.
  - w - The current relaxation parameter, a float.

op_w() compares the current iteration (n) relative change in error (defined as
the Euclidean distance between vectors) with the previous iteration (n-1)
change in error. If the error is decreasing similarly fast or faster in this
iteration, the current value for w (the relaxation parameter) is maintained .

If the speed of convergence has decreased, a new value of w is returned by
increasing or decreasing the previous w value by 0.05 within the bounds of
1.5 and 1.

Requirements: random

"""

import random

def op_w(list, w):
    change = list[-1] / list[-2]
    prev_change = (list[-2] / list[-3])
    if change > prev_change - 0.05:
        return w
    else:
        m = (random.randint(0,1) * 2 - 1)
        i = w + 0.05 * m
        if i > 1 and i < 1.5:
            return i
        else:
            return w + 0.05 * (-1 * m)