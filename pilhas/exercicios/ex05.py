class StackEx05:

    def __init__(self, capacity):
        self.capacity = capacity
        self.a = [None for _ in range(capacity)]
        self.t1 = -1
        self.t2 = capacity

    def is_full(self):
        return self.t1 == self.t2

    def is_empty(self, p):
        if p == 1:
            return self.t1 == -1

        return self.t2 == self.capacity

    def len(self, p):

        if p == 1:
            return self.t1 + 1

        return self.capacity - self.t2

    def empty(self):

        self.t1 = -1
        self.t2 = self.capacity

    def push(self, data, p):

        if not self.is_full():
            if p == 1:
                self.t1 += 1
                self.a[self.t1] = data

            else:
                self.t2 -= 1
                self.a[self.t2] = data

    def pop(self, p):

        if self.is_empty(p):
            return
        if p == 1:
            data = self.a[self.t1]
            self.t1 -= 1

        else:
            data = self.a[self.t2]
            self.t2 += 1

        return data

    def peek(self, p):
            if self.is_empty(p):
                return
            
            if p == 1:
                data = self.a[self.t1]

            else:
                data = self.a[self.t2]

            return data        
