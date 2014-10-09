class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

    
obj = C()

# Check that x is in object
print 'hasattr(obj, x) = {}'.format(hasattr(obj, 'x'))

# Set value of x
obj.x = 10

# Get value of x
print 'obj.x = {}'.format(obj.x)

# Delete x
del obj.x

# Check that x is no longer in object
print 'hasattr(obj, x) = {}'.format(hasattr(obj, 'x'))