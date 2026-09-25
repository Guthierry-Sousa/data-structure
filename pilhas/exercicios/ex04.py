class StackEx04:

    def __init__(self, capacity):
        self.capacity = capacity
        self.a = [0 for _ in range(capacity + 1)]

    def is_full(self):
        return self.a[0] == self.capacity

    def is_empty(self):
        return self.a[0] == 0

    def len(self):
        return self.a[0]

    def empty(self):

        self.a[0] = 0

    def push(self, data):

        if not self.is_full():
            self.a[0] += 1
            self.a[self.a[0]] = data

    def pop(self):

        if not self.is_empty():
            data = self.a[self.a[0]]
            self.a[0] -= 1
            return data

    def peek(self):

        if not self.is_empty():
            return self.a[self.a[0]]