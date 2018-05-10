def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3, 4], [2, 3, 4]))


def mymap2(func, *seqs):
    return (func(*args) for args in zip(*seqs))  # yielded version with (..) - generator expression


""" My zip"""
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res


print(myzip('abc', 'xyz123'))


""" My zip with iterators - supports any iterable """
def myzip2(*seqs):
    iters = list(map(iter, seqs))
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


print(list(myzip2('abc', 'xyz123')))