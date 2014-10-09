def squares(n):
    for i in xrange(n):
        yield i * i

print squares(5)
print list(squares(5))