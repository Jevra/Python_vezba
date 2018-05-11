# Trying out polymorph behavior using arbitrary arguments
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res


def min2(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]


#print(min1(3, 4, 1, 2))
#print(min2('bb', 'aa', 'cc'))


def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res


def lessthan(x, y): return x < y


def grtrthan(x, y): return x > y

# Recursion
def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)  # ternary expression


#print(mysum([1, 2, 3, 4, 5]))
#print(mysum(['spam', 'ham', 'eggs']))
#print(mysum(open('Proba').read().split()))


# list comprehension
list = [x for x in range(0, 50) if x % 3 == 0]
#print(list)

print('I am: ', __name__)
if __name__ == '__main__':
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3))
    print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))
