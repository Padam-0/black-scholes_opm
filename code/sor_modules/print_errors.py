def print_errors(error_list):
    # If any errors in the list:
    if len(error_list) != 0:
        # Print errors and exit
        exit("The following errors were identified:\n\n" + "\n".join([" -  %s" %
        (str(value)) for value in error_list]) + "\n\nPlease correct these "
        "errors and restart the program")