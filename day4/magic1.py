class MyClass:
    def __gt__(self, other):
        return getattr(self, 'x', 0) > getattr(other, 'x', 0) 

obj1 = MyClass()
obj2 = MyClass()

obj1.x = 10

print 'greater' if obj1 > obj2 else 'lesser'