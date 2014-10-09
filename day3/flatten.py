#!/usr/bin/env python

def flatten(l):
    result = []
    for item in l:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

if __name__ == '__main__':
    l = [ [1, 2, [3, 4] ], [5, 6], 7]
    print 'flatten({}) = {}'.format(l, flatten(l))

    l = [1, 2, [3, 4, [5, 6, 7], [8]]]
    print 'flatten({}) = {}'.format(l, flatten(l))