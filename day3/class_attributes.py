class A(object):
    x = 10

a = A()
b = A()

print 'a.x={} b.x={}'.format(a.x, b.x)

#a.__class__.x = 15
#print 'a.x={} b.x={}'.format(a.x, b.x)
#
#a.x = 20
#print 'a.x={} b.x={}'.format(a.x, b.x)