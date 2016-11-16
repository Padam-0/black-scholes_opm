"""

Need to write this

"""
import random

def op_w(list, w):
    change = list[-1] / list[-2]
    prev_change = (list[-2] / list[-3])
    if change > prev_change:
        return w
    else:
        m = (random.randint(0,1) * 2 - 1)
        i = w + 0.05 * m
        if i > 1 and i < 1.5:
            return i
        else:
            return w + 0.05 * (-1 * m)