import re



def read_raw_inputs(filename):
    with open(filename, 'r') as myfile:
        data = myfile.read().replace('\n', ' ')
        pattern = re.compile(r'[^0-9\.\s:]')  # Compile a Regular Expression (
        # Regex)
        if re.search(pattern, data) == None:
            return True
        else:
            return False