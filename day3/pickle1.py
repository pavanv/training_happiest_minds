import pickle

class A(object):
    pass

a = A()
a.x = 10
a.y = 20
a.z = 30

print 'a={}'.format(a.__dict__)

with open('a.pickle', 'w') as f:
    pickle.dump((a, a), f)

with open('a.pickle') as f:
    b = pickle.load(f)

print 'b={}'.format(b.__dict__)

import ipdb; ipdb.set_trace()