from sys import argv, stdin, stdout


def simplio(func):
    """
    Simple command-line IO.
    Function decorator that passes input, output file objects as arguments.
    Determines if input and output are command-line argument file names or
    STDIN and STDOUT, or mix of one of each.
    """
    argc = len(argv)
    if argc == 3:
        infile = open(argv[1], 'r')
        outfile = open(argv[2], 'w')
    elif argc == 2:
        if not stdin.isatty():
            infile = stdin
            outfile = open(argv[1], 'w')
        else:
            infile = open(argv[1], 'r')
            outfile = stdout
    elif argc == 1 and not stdin.isatty():
        infile = stdin
        outfile = stdout
    else:
        raise IOError()
    def wrapper():
        rval = func(infile, outfile)
        if not infile.closed:
            infile.close()
        if not outfile.closed:
            outfile.close()
        return rval
    return wrapper
