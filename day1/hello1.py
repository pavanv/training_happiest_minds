#!/usr/bin/env python
import sys

print "Hello, World"

mylist = sys.argv[1:3]
mystr1 = ''.join(mylist)
mystr2 = '.'.join(mylist)

print "command line args are: {}".format(mylist)

print "mystr2: {1}\nmystr1: {0}".format(mystr1, mystr2)
