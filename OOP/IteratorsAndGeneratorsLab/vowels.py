class vowels:
    vowel_list = 'aeuiyo'
    def __init__(self, word):
        self.word = word
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.word):
            if self.word[self.index].lower() in self.vowel_list:
                ch = self.word[self.index]
                self.index += 1
                return ch
            else:
                self.index += 1
                continue
        raise StopIteration()

    def iter_with_gen(self):
        return (x for x in self.word if x.lower() in self.vowel_list)



my_string = vowels('Abcedifuty0o')
for char in my_string.iter_with_gen():
    print(char)
