#!/usr/bin/env python

import sys


print 'My name is {}'.format(sys.argv[1] if len(sys.argv) > 1 else 'XYZ')

print 'My name is %s' % (sys.argv[1] if len(sys.argv) > 1 else 'XYZ')
