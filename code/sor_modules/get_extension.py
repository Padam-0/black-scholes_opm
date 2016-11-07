"""
get_extension.py

This module contains 1 function, get_ext(), which takes 1 argument:

  - filename - A string containing the path to an input file

get_ext() returns the extension of a given file name. It searches for a
period (.) followed by one or more other characters at the end of a string.

Returns a string, the extension of the file.

Requirements: re

"""

import re

def get_ext(filename):
    # Return file extension

    # Compile a Regular Expression (Regex) pattern to identify the '.'
    # character, followed by one or more other characters at the end of a string
    pattern = re.compile(r'\..+$')

    # If any matches returned:
    if re.search(pattern, filename) != None:

        # If the pattern returns a result, find the length of the match
        a = len(re.findall(pattern, filename)[0]) - 1

        # Return extension
        return filename[-a:]