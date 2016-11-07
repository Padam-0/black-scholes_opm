def info(object, spacing=4, collapse=1):
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if
                  callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" %
        (method.ljust(spacing),
        processFunc(str(getattr(object, method).__doc__)))
        for method in methodList]))

if __name__ == "__main__":
    first_line = ["Stopping Reason", "Maximum Number of Iterations",
                  "Number of Iterations", "Machine Epsilon",
                  "X Sequence Tolerance", "Residual Sequence Tolerance"]

    print('| '.join(["%s" % (heading.ljust(30)) for heading in first_line]))