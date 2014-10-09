#!/usr/bin/env python
import sys

print "Command line options"
print sys.argv
print

print "Command line args as list"
print sys.argv[1:]
print

print "Command line args as string"
print ' '.join(sys.argv[1:])
print
