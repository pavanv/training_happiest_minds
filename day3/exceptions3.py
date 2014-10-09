def avg(seq):
    result = 0
    for val in seq:
        result += convert(val)
    return result/len(seq)

def convert(val):
    try:
        val = int(val)
    except TypeError:
        print('val type is not int')
    else:
        print('inside else block')
        return val