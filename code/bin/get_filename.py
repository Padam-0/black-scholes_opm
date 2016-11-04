import os
import re

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
            file_names.append('nas_Sor.out')
        elif len(cmArgs) == 3:
            file_names.append(cmArgs[1])
            file_names.append(cmArgs[2])
        else:
            file_names = ['nas_Sor.in', 'nas_Sor.out']

         #if not check_file_exists(con_filename(file_names[0], 1)):
        if not check_file_exists(file_names[0]):
            if input("I can't find that file. Would you like to try "
                "again? [y/n]: ").upper() == 'Y':
                continue
            else:
                exit(0)

    input_file, sample_file = con_filename(file_names[0], 1)
    output_file = con_filename(file_names[1], 2, sample_file)[0]
    return input_file, output_file


def check_file_exists(filename):
    file_exists = False
    if os.path.isfile(filename):
        file_exists = True
    if os.path.isfile(os.path.join('sample_inputs', filename)):
        file_exists = True
    return file_exists



def con_filename(filename, argNum = 0, sample_file = False):
    # Takes a filename and reformats it to be in correct input style

    if 'sample_inputs' in filename:
        sample_file = True
    elif os.path.isfile(filename):
        sample_file = False
    elif os.path.isfile(os.path.join('sample_inputs', filename)):
        sample_file = True

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

    if sample_file == True and argNum == 1:
        nf = os.path.join('sample_inputs', nf)
    elif sample_file == True and argNum == 2:
        nf = os.path.join('sample_outputs', nf)

    return os.path.join('.', nf), sample_file  # Return the extension in the form
    # './filename.in'. On windows, will be '.\filename.in'