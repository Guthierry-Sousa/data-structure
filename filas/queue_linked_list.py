class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.rear = None
        self.front = None

    def is_empty(self):

        return self.front is None

    def enqueue(self, data):

        node = Node(data)

        if self.is_empty():

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = node

    def dequeue(self):

        if self.is_empty():

            raise IndexError("Fila Vazia!")

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data