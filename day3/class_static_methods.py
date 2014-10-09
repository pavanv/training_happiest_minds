class Calculator(object):
    counter = 0 
    
    def __init__(self, x=0, y=0): 
        self.x = x 
        self.y = y 

    def add(self): 
        self.update_counter()
        return self.x + self.y 

    @classmethod
    def update_counter(cls):
        cls.counter += 1
        
    @staticmethod
    def show_help():
        print 'This calculator can add'

calc = Calculator()

calc.x = 3
calc.y = 8

print 'calc.add()={} calc.counter={}'.format(calc.add(), calc.counter)

Calculator.update_counter()
calc.update_counter()
print 'calc.counter={}'.format(calc.counter)

Calculator.show_help()
calc.show_help()