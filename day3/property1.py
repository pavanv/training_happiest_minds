class C(object):
    def __init__(self):
        self._x = None
    def getx(self):
        return self._x
    def setx(self, value):
        self._x = value
    def delx(self):
        del self._x
    x = property(getx, setx, delx, "I'm the 'x' property.")
    
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