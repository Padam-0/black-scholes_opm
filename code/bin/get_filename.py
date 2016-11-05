import os
import re

"""
get_filename.py

This module contains 3 functions:

check_CM_args();
check_file_exists(); and
con_filename().

check_CM_args() takes 1 argument:

cmArgs, a list of strings of arguments passed to another module (in this
case sor.py) via the command line.

check_CM_args() checks for the existence and validity of these arguments,
which should represent input file names passed to the function by the user.
Firstly, the function checks for the existence of command line arguments. By
default, the first is always the name of the module called. If there are 2
more specified, they are assumed to be the input and output file names. If
only 1 additional argument is provided it is assumed to be the input file
name, and the user the then prompted to provide the output filename. If no
additional arguments are provided, the user is prompted to provide both an
input and output filename.

At each stage, the user can elect to use the default file names, nas_Sor.in
and nas_Sor.out

Once file names have been gathered, the validity of these is checked using
check_file_exists() (see below). If the file name is not found, the user is
given the option to try again, or exit.


check_file_exists() takes 1 argument:

filename - A string containing the location of the input or output file the
user wants to use.

The function checks two locations to see if this file exists, using the
os.path.isfile() function from the os package. This function returns true if
the file exists, and false if it does not. check_file_exists() searches for
the existence of the file name provided in two locations:

./nas_Adam_Ellis_McSweeney_prog2/code/
./nas_Adam_Ellis_McSweeney_prog2/code/sample_inputs

The sample inputs allows testing of multiple files without having them all
present in the upper level 'code' directory.


con_filename() takes 3 arguments:

filename - A string containing the location of the input or output file the
user wants to use.
argNum - The n-th argument (integer) that the user provided on the command
line, defaults to 0.
sample_file - Boolean True if the input file is contained in the
sample_inputs folder, defaults to False.

con_filename() checks if a file is present in the working directory,
or is present in sample_inputs. Depending on the location of the file that is
found, will convert the file name to the proper form.

The function returns the corrected file name and whether the input file was
found in the sample_inputs folder or not.

"""

def check_CM_args(cmArgs):
    # Checks if command line arguments are present, and if not, collects
    # input and output file names. Checks if input files exist.

    # Initialize blank file names list
    file_names = []

    # Until there are 2 entries in the file names list (one input, one output):
    while len(file_names) != 2:
        # If there is only 1 command line argument ('sor.py') and no file
        # names:
        if len(cmArgs) == 1:
            # Ask the user to define input and output file names
            question = input('Would you like to define an input and output '
                             'filename? [y/n]: ').upper()
            # If the user wants to enter file names:
            if question == 'Y':
                # Append input and output file names to the file name list
                file_names.append(input("Please enter an input file name: "))
                file_names.append(input("Please enter an output file name: "))
            # If the user doesn't want to enter file names:
            elif question == 'N':
                # Asks the user if they want to use the default file names
                if input('Is using the default file names ok? [y/n]: '
                                     '').upper() =='Y':
                    # Append default file names to the file name list
                    file_names.append('nas_In.out')
                    file_names.append('nas_Sor.out')
                # If not, ask to exit
                else:
                    # If user elects to exit
                    if input('Would you like to exit? [y/n]: ').upper() == 'Y':
                        exit()
                    # If not, restart while loop
                    else:
                        continue
            else:
                # If user answers neither Y or N
                if input('Looks like an error. Would you like to try '
                                    'again? [y/n]: ').upper() =='Y':
                    continue
                else:
                    exit(0)

        elif len(cmArgs) == 2:
            file_names.append(cmArgs[1])
            question = input('Would you like to define an output '
                             'filename? [y/n]: ').upper()
            if question == 'Y':
                file_names.append(input("Please enter an output file name: "))
            elif question == 'N':
                if input('Is using the default file name ok? [y/n]: '
                                     '').upper() =='Y':
                    file_names.append('nas_Sor.out')
                else:
                    if input('Would you like to exit? [y/n]: ').upper() == 'Y':
                        exit("Default Exit Message")
                    else:
                        continue
        elif len(cmArgs) == 3:
            file_names.append(cmArgs[1])
            file_names.append(cmArgs[2])
        else:
            file_names = ['nas_Sor.in', 'nas_Sor.out']

        if not check_file_exists(con_filename(file_names[0], 1)[0]):
            if input("I can't find that file. Would you like to try "
                "again? [y/n]: ").upper() == 'Y':
                continue
            else:
                exit(0)

    input_file, sample_file = con_filename(file_names[0], 1)
    output_file = con_filename(file_names[1], 2, sample_file)[0]
    return input_file, output_file


def check_file_exists(filename):
    # Return True if the file exists in ./code/ or ./code/sample_inputs/
    # directories
    return os.path.isfile(filename) or os.path.isfile(os.path.join(
        'sample_inputs', filename))


def con_filename(filename, argNum = 0, sample_file = False):
    # Takes a filename and re-formats it to be in correct input style

    # Checks if the file is in the sample_inputs file
    if 'sample_inputs' in filename or os.path.isfile(os.path.join(
            'sample_inputs', filename)):
        sample_file = True

    # If the input file is in sample_inputs directory but path is incorrect,
    # prepends the correct path
    if 'sample_inputs' not in filename and sample_file == True:
        if argNum == 1:
            filename = os.path.join('sample_inputs', filename)
        elif argNum == 2:
            filename = os.path.join('sample_outputs', filename)

    return filename, sample_file