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


"""


def check_CM_args(cmArgs):
    file_names = []
    while len(file_names) != 2:
        if len(cmArgs) == 1:
            question = input('Would you like to define an input and output '
                             'filename? [y/n]: ').upper()
            if question == 'Y':
                file_names.append(input("Please enter an input file name: "))
                file_names.append(input("Please enter an output file name: "))
            elif question == 'N':
                if input('Is using the default file names ok? [y/n]: '
                                     '').upper() =='Y':
                    file_names.append('nas_In.out')
                    file_names.append('nas_Sor.out')
                else:
                    if input('Would you like to exit? [y/n]: ').upper() == 'Y':
                        exit("Default Exit Message")
                    else:
                        continue
            else:
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
    # Takes a filename and reformats it to be in correct input style

    if os.path.join('a', 'b') == 'a/b':  # Checks if OS is Mac/Unix, which uses
        #  the '/' character in directory paths
        # os is unix

        # Count number of '/' characters in the string
        c = filename.count('/')

        # If there are not 0 '/' characters present:
        if c != 0:
            # If '/' characters are present, replaces all but the last of
            # these. Then finds the index of the last '/'
            i = filename.replace('/', '|', c - 1).find('/')
            # Strips all information prior to and including the last '/',
            # leaving only the filename without a path.
            nf = filename[i + 1:]
        else:
            # If no '/' characters are found, filename is left unchanged
            nf = filename
    else:
        # os is windows

        # Count number of '\' characters in the string
        c = filename.count('\\')

        # If there are not 0 '\' characters present:
        if c != 0:
            # If '\' characters are present, replaces all but the last of
            # these. Then finds the index of the last '\'
            i = filename.replace('\\', '|', c - 1).find('\\')
            # Strips all information prior to and including the last '\',
            # leaving only the filename without a path
            nf = filename[i + 1:]
        else:
            # If no '\' characters are found, filename is left unchanged
            nf = filename

    nf = format_extension(nf, argNum)

    if 'sample_inputs' in filename:
        sample_file = True
    elif os.path.isfile(nf):
        sample_file = False
    elif os.path.isfile(os.path.join('sample_inputs', nf)):
        sample_file = True

    # If all else fails
    filename = format_extension(filename, argNum)
    if os.path.isfile(filename):
        return filename, sample_file

    if sample_file == True and argNum == 1:
        nf = os.path.join('sample_inputs', nf)
    elif sample_file == True and argNum == 2:
        nf = os.path.join('sample_outputs', nf)

    return os.path.join('.', nf), sample_file  # Return the extension in the form
    # './filename.in'. On windows, will be '.\filename.in'

def format_extension(filename, argNum):

    pattern = re.compile(r'\..+$')  # Compile a Regular Expression (Regex)
    # pattern to identify the '.' character, followed by one or more other
    # characters at the end of a string
    if re.search(pattern, filename) != None:
        # If the pattern returns a result, find the length of the match
        a = len(re.findall(pattern, filename)[0])
        nf = filename[:-a]  # Remove the file extension from the end of the
        # filename
    if argNum == 1:
        filename += '.in'  # Replace the file extension with '.in'
    elif argNum == 2:
        filename += '.out'  # Replace the file extension with '.out'

    return filename