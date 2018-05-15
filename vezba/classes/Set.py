class Set(object):
    def __init__(self, value = []):
        self.data = []
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        res.sort()
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        res.sort()
        return Set(res)

    def concat(self, value):
        for x in value:
            if not x in self.data:
                self.data.append(x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + repr(self.data)

    def __iter__(self):
        return iter(self.data)


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    print(x.union(Set([1, 4, 6])))
    print(x | Set([1, 4, 6]))
    print(x & Set([1, 5, 7]))


    word_list = ['cat', 'dog', 'rabbit']
    letter_list = []
    for a_word in word_list:
        for a_letter in a_word:
            if a_letter not in letter_list:
                letter_list.append(a_letter)
    print(letter_list)

    letter_list1 = {a_letter for a_word in word_list for a_letter in a_word}
    print(list(letter_list1))


    string = list('methinks it is like a weasel')
    elements = 'abcdefghijklmnopqrstuvwxyz '

    def score(string, generated_string):
        return string == elements

    def generate():
        import random
        generated_string = random.choices(elements, k=28)
        i = 0
        while i < len(string) and i < len(generated_string):
            while string[i] != generated_string[i]:
                generated_string[i] = random.choice(elements)
                print(generated_string)
            i += 1


        print('I Got It!!!')

    generate()



