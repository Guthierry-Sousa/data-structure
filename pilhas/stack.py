class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Stack:

    def __init__(self):

        self.head = None

    def push(self, data):

        node = Node(data)
        node.next = self.head
        self.head = node



    def pop(self):

        if self.head:

            temp = self.head.data
            self.head = self.head.next

            return temp


        else:

            raise IndexError("Stack Underflow")


    def peek(self):

        if self.head is None:

            return None

        return self.head.data

    def is_empty(self):

        return self.head is None



            
