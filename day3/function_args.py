def func1(*args):
    for ndx, item in enumerate(args):
        print 'args[{}] = {}'.format(ndx, item)

#func1('a', 'b', 'c')

func1('a', 'b', c='c')