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
    # Calculate relative change in error on current iteration
    change = list[-1] / list[-2]

    # Calulate relative change in error on previous iteration
    prev_change = (list[-2] / list[-3])

    # If current change is similar or faster than previous change:
    if change > prev_change - 0.05:
        # Keep same w
        return w
    # Otherwise
    else:
        # Choose a random direction up or down
        m = (random.randint(0,1) * 2 - 1)

        # Add / Subtract 0.05 from w
        new_w = w + 0.05 * m

        # If new value for w is within 1 and 1.5 inclusive
        if new_w >= 1 and new_w <= 1.5:
            # Return new w value
            return new_w
        # Otherwise
        else:
            # Return w +/- 0.05 in the other direction
            return w + 0.05 * (-1 * m)


list = [0.6, 0.7, 0.79, 0.7, 0.8]
w = 1.2

print(op_w(list, w))