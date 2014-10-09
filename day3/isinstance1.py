class A(object):
    pass

class B(A):
    pass

class C(object):
    pass

a = A()
b = B()
c = C()

#print 'type(a) = {}'.format(type(a))
#print 'type(A) = {}'.format(type(A))

#print 'type(a) == A: {}'.format(type(a) == A)

#print 'isinstance(a, A)={} isinstance(a, B)={} isinstance(a, C)={}'.format(
#    isinstance(a, A), isinstance(a, B), isinstance(a, C))
#print 'isinstance(b, A)={} isinstance(b, B)={} isinstance(b, C)={}'.format(
#    isinstance(b, A), isinstance(b, B), isinstance(b, C))
#print 'isinstance(c, A)={} isinstance(c, B)={} isinstance(c, C)={}'.format(
#    isinstance(c, A), isinstance(c, B), isinstance(c, C))

#print 'issubclass(A, A)={} issubclass(A, B)={} issubclass(A, C)={}'.format(
#    issubclass(A, A), issubclass(A, B), issubclass(A, C))
#print 'issubclass(B, A)={} issubclass(B, B)={} issubclass(B, C)={}'.format(
#    issubclass(B, A), issubclass(B, B), issubclass(B, C))
#print 'issubclass(C, A)={} issubclass(C, B)={} issubclass(C, C)={}'.format(
#    issubclass(C, A), issubclass(C, B), issubclass(C, C))