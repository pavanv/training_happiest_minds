def func1(*args, **kwargs):
    for ndx, item in enumerate(args):
        print 'args[{}] = {}'.format(ndx, item)

    for key, val in kwargs.items():
        print 'kwargs[{}] = {}'.format(key, val)

    print '-' * 30


func1(*['a', 'b', 'c'])

func1(**{'a': 1, 'b': 2, 'c': 3})

func1(*['a', 'b'], **{'c': 'c'})