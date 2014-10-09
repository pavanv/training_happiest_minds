import sys

def num_occurs(s):
    d = {}
    for c in s:
        d[c] = d.get(c, 0) + 1
    for item in sorted(d.items()):
        print '{} {}'.format(item[0], item[1])

num_occurs(sys.argv[1]) 