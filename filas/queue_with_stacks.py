import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pilhas.stack_arrays import StackArrayDynamic

class QueueWithStacks:

    def __init__(self):

        self.stack1 = StackArrayDynamic()
        self.stack2 = StackArrayDynamic()

    def enqueue(self, data): # O(1)

        self.stack1.push(data)

    def dequeue(self): # O(n)

        while (self.stack1.is_empty() == False):

            self.stack2.push(self.stack1.pop())

        data = self.stack2.pop()

        while (self.stack2.is_empty() == False):

            self.stack1.push(self.stack2.pop())

        return data

    def is_empty(self):
        return self.stack1.is_empty()


        

    