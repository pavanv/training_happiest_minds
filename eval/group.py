import math

def group(l, sz):
    nloops = int(math.ceil(len(l) * 1.0 / sz))
    result = []
    for i in range(nloops):
        result.append(l[i * sz: i * sz + sz])
    return result