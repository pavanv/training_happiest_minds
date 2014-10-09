def cumulative_sum(l):
    cs = 0
    for x in l:
        val = cumulative_sum(x) if type(x) == list else x
        cs += val
    return cs