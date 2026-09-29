from queue_linked_list import Queue

class StackWithQueue:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, data):
        self.q1.enqueue(data)

    def pop(self):

        data = None

        if self.q1.is_empty():
            raise IndexError("Pilha está vazia")

        while not self.q1.is_empty():

            data = self.q1.dequeue()

            if self.q1.is_empty():
                break

            self.q2.enqueue(data)

        self.q1, self.q2 = self.q2, self.q1

        return data

    def is_empty(self):

        return self.q1.is_empty() and self.q2.is_empty()
            

        
