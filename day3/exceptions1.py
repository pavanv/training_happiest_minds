def avg(seq):
    result = 0
    for val in seq:
        result += convert(val)
    return result/len(seq)

def convert(val):
    try:
        val = int(val)
    except ValueError:
        raise ValueError('val type is not int')
    return val

#print avg([1, 2, 4, 5])
print avg([1, 'two', 4, 5])