class Calculator(): 
    counter = 0 
    
    def __init__(self, x=0, y=0): 
        self.x = x 
        self.y = y 

    def add(self): 
        self.__class__.counter += 1 
        return self.x + self.y

calc = Calculator(10, 20) 
print calc.add()      
print 'calc.counter={}'.format(calc.counter)    # 1

calc2 = Calculator(30, 40) 
print calc2.add()     
print 'calc2.counter={}'.format(calc2.counter)   # 2

calc.counter = 10

print 'calc.counter={}'.format(calc.counter)
print 'calc2.counter={}'.format(calc2.counter)

print 'calc.__class__.counter={}'.format(calc.__class__.counter)
