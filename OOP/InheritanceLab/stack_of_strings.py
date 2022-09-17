class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        element = self.data.pop()
        return element

    def top(self):
        return self.data[len(self.data) - 1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        result = "["
        result += ", ".join(reversed(self.data))
        result += "]"
        return result

# stack = Stack()
# stack.push("apple")
# stack.push("carrot")
# print(stack)
# stack.push("cucumber")
# print(stack)



