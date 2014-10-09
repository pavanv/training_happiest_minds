#func1 = lambda x: x * 2, x * 3;

def double_triple(x):
    # this function returns double and triple of the input
    return x * 2, x * 3;


double, triple = double_triple(10)

print 'double={} triple={}'.format(double, triple)