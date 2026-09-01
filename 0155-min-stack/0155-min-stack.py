class MinStack(object):

    def __init__(self):
        self.items = []
        self.minvalue = []

    def push(self, value):
        self.items.append(value)

        if not self.minvalue or value <= self.minvalue[-1]:
            self.minvalue.append(value)

    def pop(self):
        if self.items[-1] == self.minvalue[-1]:
            self.minvalue.pop()

        self.items.pop()

    def top(self):
        return self.items[-1]

    def getMin(self):
        return self.minvalue[-1]
