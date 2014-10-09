class A(object):
    def __init__(self):
        self.a = 'a'

class B(A):
    def __init__(self):
        self.b = 'b'

b = B()
print 'b={}'.format(b.__dict__)