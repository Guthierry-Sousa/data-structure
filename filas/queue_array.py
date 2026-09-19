class QueueArray: 

    def __init__(self, size):
        self.front = self.rear = -1
        self.size = size

        self.__queue = [None for _ in range(size)]

    def is_empty(self):

        return self.front == -1

    def is_full(self):

        return (self.rear + 1) % self.size == self.front


    def enqueue(self, data):

        if self.is_full():
            raise OverflowError("Fila cheia!")

        if self.is_empty():
            self.front = self.rear = 0

        else:
            self.rear = (self.rear + 1) % self.size

        self.__queue[self.rear] = data

    def dequeue(self):

        if self.is_empty():
            raise IndexError("Fila vazia!")

        data = self.__queue[self.front]

        if self.front == self.rear:

            self.front = self.rear = -1

        else:

            self.front = (self.front + 1) % self.size

        return data 