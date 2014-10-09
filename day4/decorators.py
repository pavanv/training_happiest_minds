def outer1():
    x = 1
    def inner():
        print x
    inner()


def outer2():
    def inner():
        print "Inside inner"
    return inner


def outer3():
    x = 1
    def inner():
        print x
    return inner


def outer4(x):
    def inner():
        print x
    return inner


def outer5(some_func):
    def inner():
        print "before some_func"
        ret = some_func()
        return ret + 1
    return inner


def foo():
    return 1


def logger(func):
    def inner(*args, **kwargs):
        print "Arguments were: %s, %s" % (args, kwargs)
        return func(*args, **kwargs)
    return inner


@logger
def foo1(x, y=1):
    return x * y

@logger
def foo2():
    return 2


if __name__ == '__main__':

    decorated = outer5(foo)
    print 'decorated={}'.format(decorated())

    foo1(5, 4)
    foo1(1)
    foo2()