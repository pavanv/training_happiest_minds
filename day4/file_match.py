import sys
import re

def match_file(filename, pattern):
    try:
        with open(filename) as f:
            lines = f.readlines()
    except Exception, e:
        print 'Got exception: {}'.format(e)
        lines = []

    # Remove the newline characters
    lines = [line.rstrip('\n') for line in lines]

    # Loop through the lines searching for the pattern
    for ndx, line in enumerate(lines):
        match = re.search(pattern, line)
        if not match:
            continue
        print '{}:{}'.format(ndx + 1, line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'Usage: {} <filename> <pattern>'.format(sys.argv[0])
        sys.exit(1)

    match_file(sys.argv[1], sys.argv[2])