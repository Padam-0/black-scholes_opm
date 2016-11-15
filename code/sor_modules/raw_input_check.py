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
from sor_modules import write_output

def read_raw_inputs(filename, output_filename):
    with open(filename) as f:
        first_line = f.readline().strip()

        # Set errors to 0
        errors = 0

        # Compile a Regular Expression (Regex) to check for any characters
        # that are not digits, the decimal point character, or whitespace.
        pattern = re.compile(r'[^0-9\.\s:]')
        data = first_line.replace('\n', ' ')
        if re.search(pattern, data) != None:
            write_output.output_text_file(output_filename, "Cannot Proceed")
            exit("First line contains non-digit entries. Please fix and try "
                 "again")

        # If the matrix is dense
        if len(first_line.split(' ')) == 1:
            # For for the next n lines
            for i in range(int(first_line) + 1):
                # Read the line into memory
                line_in = f.readline()
                # Replace newline characters with spaces
                data = line_in.replace('\n', ' ')
                # Return True if a search of the data returns no matches for
                # characters other than those allowed, otherwise returns False
                if re.search(pattern, data) != None:
                    errors += 1
        # Else if the matrix is CSR
        else:
            for i in range(4):
                # Read the line into memory
                line_in = f.readline()
                # Replace newline characters with spaces
                data = line_in.replace('\n', ' ')
                # Compile a Regular Expression (Regex) to check for any characters
                # that are not digits, the decimal point character, or whitespace.
                pattern = re.compile(r'[^0-9\.\s:]')

                # Return True if a search of the data returns no matches for
                # characters other than those allowed, otherwise returns False
                if re.search(pattern, data) != None:
                    errors += 1

    if errors != 0:
        return False