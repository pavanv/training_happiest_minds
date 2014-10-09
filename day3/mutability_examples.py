#!/usr/bin/env python


def f1(s):
    s = 'This is the new string'
    #s += ' I have been appended'

def f2(l):
    l = ['This is a new list']

def f3(l):
    l.append('This is a new list')

mystr = 'Hello, World'
#f1(mystr)
#print 'mystr={}'.format(mystr)
#
#mylist1 = [mystr]
#f2(mylist1)
#print 'mylist1={}'.format(mylist1)
#
mylist2 = [mystr]
f3(mylist2)
print 'mylist2={}'.format(mylist2)