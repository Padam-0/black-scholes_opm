"""
print_errors.py

This module contains 1 function, print_errors(), which takes 1 argument:

  - error_list - A list of strings of errors in a file

if error_list has any contents, print_errors() returns the errors to the user
in an appropriate format, before exiting the program

Requirements: None

"""

def print_errors(error_list):
    # If any errors in the list:
    exit("The following errors were identified:\n\n" + "\n".join([" -  %s" %
        (str(value)) for value in error_list]) + "\n\nPlease correct these "
        "errors and restart the program")