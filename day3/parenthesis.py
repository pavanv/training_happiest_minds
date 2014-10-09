#!/usr/bin/env python

def parenthesis(s):
    num_left = num_right = 0
    for c in s:
        if c not in ['(', ')']:
            continue
        if c == '(':
            num_left += 1
        if c == ')':
            num_right += 1
        if num_left < num_right:
            return False
    return True if num_left == num_right else False
