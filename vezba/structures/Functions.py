import vezba.structures.mins

def echo(message):
    print(message)


listOfToDo = [(echo, 'Spam'), (echo, 'Jevra')]

for (func, arg) in listOfToDo:
    func(arg)


func = echo
func('Hej')
print(func.__name__)


# lambda
def knights():
    title = 'Sir'
    function = lambda x: title + ' ' + x.title()
    return function


act = knights()
msg = act('robin')
print(msg)

L = [lambda x: x**2,
     lambda x: x**3,
     lambda x: x**4]

print(L[1](3))


# yield
def gen():
    for i in range(10):
        X = yield
        yield X**2
        print(X)


G = gen()
next(G)
print(G.send(8))
next(G)
print(G.send(3))
next(G)