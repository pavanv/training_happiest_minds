def mysum(l):
    if not l:
        return 0
    val = '' if type(l[0]) == str else 0
    for x in l:
        val += x

    return val