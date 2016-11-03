import numpy as np
import sys

def check_CM_args(cmArgs):
    if len(cmArgs) == 1:
        #prompt user
        if userNoreply:
            input_file = 'nas_In.out'
            output_file = 'nas_Sor.out'
    elif len(cmArgs) == 2:
        input_file = cmArgs[1]
        output_file = 'nas_Sor.out'
    elif len(cmArgs) == 3:
        input_file = cmArgs[1]
        output_file = cmArgs[2]
    else:
        exit()
    return input_file, output_file


def read_inputs(filename):
    # Open a file and extract data
    try:
        matrix_size = np.genfromtxt(filename, max_rows=1)
        # print('Matrix size n:',matrix_size)
        # print('----------')

        matrix_in = np.genfromtxt(filename, skip_header=1, skip_footer=1)
        # print('Matrix A:')
        # print(matrix_in)
        # print('----------')

        column = np.genfromtxt(filename, usecols=0)
        col_len = len(column)
        # print('Column length', col_len)
        # print('----------')

        vector_b = np.genfromtxt(filename, skip_header=(col_len - 1))
        # print('Vector b: ',vector_b)

        return matrix_size, matrix_in, vector_b

    except:
        o = input("I can't find a file with that name. If you want to quit, "
              "please press Q, if not, please try again:  ").upper()
        if o == 'Q':
            exit(0) # If filename is wrong, allow user option to quit (Q)
        else:
            read_inputs(getfilename(o.lower())) # If filename is wrong,
            # allow user option to keep trying


def con_to_csr(matrix, matrix_length):
    # Convert an numpy array to CSR Structure
    val = np.ndarray.flatten(matrix)
    col = []
    rowStart = []
    pos = 0
    zeros = 0
    for entry in np.nditer(matrix):
        if entry != 0:
            col.append((pos) % matrix_length)
            if pos % matrix_length == 0:
                rowStart.append(pos - zeros)
        else:
            zeros += 1
        pos += 1
    rowStart.append(len(col))

    val = [i for i in val if i != 0]
    col = np.array(col)
    rowStart = np.array(rowStart)

    return val, col, rowStart


def write_outputs(solution_vector, stopping_reason, other_information):
    pass


def matrix_det(matrix):
    # check that matrix determinant is non zero
    if np.linalg.det(matrix) != 0:
        return True
    else:
        return False


def zero_diag(val, col, rowStart):
    # Check if there are 0's on the diagonal of the input matrix

    row = 0
    tf = True
    for i in range(len(rowStart)-1):
        r = col[rowStart[i]:rowStart[i+1]]
        if row not in r:
            tf = False
        row += 1

    return tf


def diag_dominant(val, col, rowStart):
    # Check if the diagonal value is larger than the sum of all
    # other entries in that row/column

    diags = []
    col_sums = []
    row_sums = []
    for i in range(len(rowStart) - 1):
        # 0 through 2
        r = col[rowStart[i]:rowStart[i + 1]]

        if i in r:
            diags.append(val[rowStart[i] + int(np.where(r == i)[0])])

        c_sum = 0
        for j in range(len(col)):
            if col[j] == i:
                c_sum += val[j]
        col_sums.append(c_sum)

        row_sums.append(sum(val[rowStart[i]:rowStart[i + 1]]))

    diags = np.asarray(diags)
    col_sums = np.array(col_sums) - diags
    row_sums = np.array(row_sums) - diags

    if np.greater(diags, col_sums).all() and np.greater(diags,row_sums).all():
        return True
    else:
        return False

def getfilename(filename):
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
    nf += '.txt'  # Replace the file extension with '.txt'
    return os.path.join('..', nf)  # Return the extension in the form
    # '../filename.txt'. On windows, will be '..\filename.txt'

