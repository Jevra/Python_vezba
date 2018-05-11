class Person(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaies(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)

    def giveRaies(self, percent, bonus=.10):
        return Person.giveRaies(self, percent + bonus)


if __name__ == '__main__':
    # test
    jevra = Person('Nikola Jevremovic', 'dev', 100000)
    print(jevra)
    jevra.giveRaies(.10)
    print(jevra)
    tamara = Manager('Tamara Panic', 100000)
    tamara.giveRaies(.10)
    print(tamara)
    print(tamara.lastName())

    import shelve
    db = shelve.open('persondb')
    for obj in(jevra, tamara):
        db[obj.name] = obj
    db.close()

    import glob
    print(glob.glob('person*'))


    temp = shelve.open('persondb')
    for pom in list(temp.keys()):
        print(pom + ': ' + str(temp[pom]))
    temp.close();

    print(open('persondb', 'rb').read())

    """ Kada zelim da importujem podatke iz shelve-a, nema potrebe importovati klase cije su instance cuvane u shelvu
    jer shelve to samo reimportuje jer cuva i self atribut, kao i ime klase kojoj objekat pripada"""
