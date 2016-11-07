"""
raw_input_check.py

This module contains 1 function, vectornorm(), which takes 1 argument.
This is:

v - A 1 Dimensional Numpy array containing n elements, all floats.

The purpose of vectornorm() is to calculate the euclidean norm of a given
vector. In this context, the norm of the vector v (||v||) is defined as:

||v|| = sqrt(v1^2 + v2^2 +... +vn^2)

Or the square root of the sum of the squares of all the individual entries
of the vector.

vectornorm() returns a float value that is the norm of the vector v.

Requirements: math

"""

import math

def vectornorm(vector):
    # Calculate the norm of the input vector

    # Initialize norm to 0
    sum_of_squares = 0
    # For each element in the vector
    for element in vector:
        # Increase the sum of squares by the square of the given element
        sum_of_squares += element ** 2

    # Return the square root of the sum of squares, or the norm of the vector
    return math.sqrt(sum_of_squares)