#!/usr/bin/env python
import sys


def fib1(n):
    return [0, 1][n] if n < 2 else fib1(n - 1) + fib1(n - 2)


def fib2(n):
    a, b = 0, 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(n - 1):
        a, b = b, a + b
    return b


def fib3(n):
    l = [0, 1]
    if n < 2:
        return l[n]
    for i in range(n - 1):
        l.append(l[-1] + l[-2])
    return l[-1]


if __name__ == '__main__':
    n = int(sys.argv[1])
    print 'fib1({}) = {}'.format(n, fib1(n - 1))
    print 'fib2({}) = {}'.format(n, fib2(n - 1))
    print 'fib3({}) = {}'.format(n, fib3(n - 1))