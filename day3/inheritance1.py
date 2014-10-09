class Shape(object): 
    def name(self, shape): 
        print "Shape: %s" % shape 

class Square(Shape): 
    def name(self, shape): 
        super(Square, self).name(shape) 
        print "Child class Shape %s" % shape 
     
    def area(self, side): 
        return side**2 
