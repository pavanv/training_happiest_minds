import sys


def get_first(arg):
    return arg[1]


def count_words(filename):
    results = {}
    with open(filename, 'r') as f:
        for line in f:
            for word in line.split():
                results[word] = results.get(word, 0) + 1

    for word, count in sorted(results.items(), lambda x, y: x[1]):
        print('{} {}'.format(count, word))

count_words(sys.argv[1])
