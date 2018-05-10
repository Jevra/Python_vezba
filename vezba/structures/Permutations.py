def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute1(rest):
                res.append(seq[i:i+1] + x)
        return res


print(permute1('abc'))


""" Koliko shvatam, uzima jedan element iz sekvence i doda ga kasnije """


def permute2(seq):
    if not seq:
        yield seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x


print(list(permute2('abc')))

G = permute2('aab')
print(next(G))
print(next(G))

p = permute2(list(range(50)))
for x in p:
    print(x)