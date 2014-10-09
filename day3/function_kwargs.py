def func1(**kwargs):
    for key, val in kwargs.items():
        print 'kwargs[{}] = {}'.format(key, val)

#func1(a=1, b=2, c=3)

func1(1, 2, c='c')