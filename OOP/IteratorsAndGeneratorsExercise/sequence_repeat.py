class sequence_repeat:
    def __init__(self, word, n):
        self.word = word
        self.n = n
        self.index = 0
        self.local_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.n:
            if self.local_index < len(self.word):
                result = self.word[self.local_index]
                self.local_index += 1
                self.index += 1
                return result
            else:
                self.local_index = 0
                result = self.word[self.local_index]
                self.local_index += 1
                self.index += 1
                return result
        raise StopIteration()


result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')