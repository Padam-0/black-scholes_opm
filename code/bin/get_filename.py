import os
import re

def check_CM_args(cmArgs):
    in_names = []
    while len(in_names) != 2:
        if len(cmArgs) == 1:
            question = input('Would you like to define an input and output '
                             'filename? [y/n]: ').upper()
            if question == 'Y':
                in_names.append(input("Please enter an input file name: "))
                if not check_file_exists(in_names[0]):
                    if input(
                        "I can't find that file. Would you like to try "
                        "again? [y/n]: ").upper() == 'Y':
                        continue
                    else:
                        exit(0)
                in_names.append(input("Please enter an output file name: "))
            elif question == 'N':
                if input('Is using the default file names ok? [y/n]: '
                                     '').upper() =='Y':
                    in_names.append('nas_In.out')
                    in_names.append('nas_Sor.out')
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
            in_names.append(cmArgs[1])
            in_names.append('nas_Sor.out')
        elif len(cmArgs) == 3:
            in_names.append(cmArgs[1])
            in_names.append(cmArgs[2])
        else:
            in_names = ['nas_Sor.in', 'nas_Sor.out']

    input_file = con_filename(in_names[0], 1)
    output_file = con_filename(in_names[1], 2)
    return input_file, output_file


def check_file_exists(filename):
    return os.path.isfile(filename)


def con_filename(filename, argNum = 0):
    # Takes a filename and reformats it to be in correct input style
    if os.path.join('a', 'b') == 'a/b':  # Checks if OS is Mac/Unix, which uses
        #  the '/' character in directory paths
        # os is unix
        c = filename.count('/')  # Counts number of '/' characters in the string
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
        c = filename.count('\\')  # Counts number of '\' characters
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

    pattern = re.compile(r'\..+$')  # Compile a Regular Expression (Regex)
    # pattern to identify the '.' character, followed by one or more other
    # characters at the end of a string
    if re.search(pattern, nf) != None:
        # If the pattern returns a result, find the length of the match
        a = len(re.findall(pattern, nf)[0])
        nf = nf[:-a]  # Remove the file extension from the end of the filename
    if argNum == 1:
        nf += '.in'  # Replace the file extension with '.in'
    elif argNum == 2:
        nf += '.out'  # Replace the file extension with '.out'
    return os.path.join('.', nf)  # Return the extension in the form
    # '../filename.txt'. On windows, will be '..\filename.txt'