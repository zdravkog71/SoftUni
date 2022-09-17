class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.i = len(self.iter_obj) - 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.i >= 0:
            n = self.i
            self.i -= 1
            return self.iter_obj[n]
        else:
            raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)