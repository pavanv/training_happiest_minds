import sys


def count_words(filename):
    count = 0
    with open(filename, 'r') as f:
        for line in f:
            count += len(line.split())
    print '{} has {} words'.format(filename, count)

count_words(sys.argv[1])
