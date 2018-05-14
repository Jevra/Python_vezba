class Super:
    def method(self):
        print('In Super.method')

    def delegate(self):
        self.action()


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('In Replacer.method')


class Extender(Super):
    def method(self):
        print('Starting Extender.method')
        Super.method(self)
        print('Ending Extender.method')


class Provider(Super):
    def action(self):
        print('In Provider.action')


class Commuter:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other

    # __radd__ = __add__

    def __radd__(self, other):
        return self.__add__(other)

if __name__ == '__main__':
    for c in (Inheritor, Replacer, Extender):
        print('\n' + c.__name__ + '...')
        c().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()


    a = Commuter(5)
    b = Commuter(10)

    a + 1
    1 + a
    a + b