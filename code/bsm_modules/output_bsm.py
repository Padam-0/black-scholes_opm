"""

To be written

"""

def output_bsm(output_filename, option_val, s, X, T, sigma, r):
    with open(output_filename, 'w') as f:
        # Output solution_vector_x, stopping_reason, maxits, #_of_iterations,
        # machine_epsilon, x-seq_tolerance, residual, w

        # Create headings list, along with spacings
        headings = [["Option Value", 15],
                      ["Stock Price today", 20],
                      ["Strike Price", 15], ["Days to Maturity", 19],
                      ["Volatility", 13],
                      ["Risk Free Rate", 17]]

        # Create values list, along with spacings
        values = [["$%.2f" % (option_val), 15],
                      ["$%.2f" % (s), 20],
                      ["$%.2f" % (X), 15], ["%.2f" % (T), 19],
                      ["%.2f" % (sigma), 13],
                      ["%.2f" % (r), 17]]

        # Output headings
        f.write('| '.join(["%s" % (heading[0].ljust(heading[1])) for heading in
                           headings]))
        f.write("\n")
        # Output values from second_line
        f.write('| '.join(["%s" % (value[0].ljust(value[1]))for value in
                           values]))