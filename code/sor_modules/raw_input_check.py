"""
raw_input_check.py

This module contains 1 function, read_raw_inputs(), which takes 1 argument.
This is:

  - filename - A string containing the location of the input or output file the
user wants to use.

read_raw_inputs() aims to check all values of the input file to ensure they
are either digits (0-9), the decimal point character (.) or whitespace. These
are the only data allowed in the input file, and would crash the program if
it was attempted to convert such entries into a numpy array, which by
definition can only take a single data type.

read_raw_inputs() returns a boolean value, denoting whether the input file
contains only the allowed characters or not.

Requirements: re

"""

import re

def read_raw_inputs(filename):
    # Open the input file
    with open(filename, 'r') as myfile:
        # Replace newline characters with spaces
        data = myfile.read().replace('\n', ' ')
        # Compile a Regular Expression (Regex) to check for any characters
        # that are not digits, the decimal point character, or whitespace.
        pattern = re.compile(r'[^0-9\.\s:]')

        # Return True if a search of the data returns no matches for
        # characters other than those allowed, otherwise returns False
        return re.search(pattern, data) == None