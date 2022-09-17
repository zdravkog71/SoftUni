class dictionary_iter:
    def __init__(self, dict_obj):
        self.dict_obj = dict_obj
        self.index = 0
        self.dict_list = list(self.dict_obj.items())

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.dict_obj):
            i = self.index
            self.index += 1
            return self.dict_list[i]
        else:
            raise StopIteration()




result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)