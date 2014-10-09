import sys

print "hasattr(sys, 'argv') = {}".format(hasattr(sys, 'argv'))

print "getattr(sys, 'argv') = {}".format(getattr(sys, 'argv'))

#print "getattr(sys, 'doesnotexist') = {}".format(getattr(sys, 'doesnotexist'))

print "getattr(sys, 'doesnotexist', 'default') = {}".format(getattr(sys, 'doesnotexist', 'default'))