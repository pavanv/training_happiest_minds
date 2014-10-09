import sys

class MyException(Exception):
    pass

def divide(num):
    try:
        return 100/num
    except ZeroDivisionError:
        raise MyException('Cannot divide by 0')

try:
    result = divide(float(sys.argv[1]))
except MyException, e:
    print 'Caught MyException: {}'.format(e)
except ValueError:
    print '{} is not a number'.format(sys.argv[1])
except IndexError:
    print 'Usage: {} <number>'.format(sys.argv[0])
else:
    print 'result = {}'.format(result)