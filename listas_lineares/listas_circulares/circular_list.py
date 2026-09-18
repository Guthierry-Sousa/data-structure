from node import Node

class CircularList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def insertion_at_beginning(self, data): # O(1)

        node = Node(data=data)

        if self.size == 0:

            self.head = node
            node.next = self.head

        else:

            node.next = self.head

            current = self.head

            while current.next != self.head:
                current = current.next

            current.next = node
            self.head = node

        self.size += 1
        

    def insertion_at_end(self, data): # O(n)

        node = Node(data=data)

        if self.size == 0:

            self.head = node
            node.next = self.head

        else:
            
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = node
            node.next = self.head

        self.size += 1



    def insert_at_given_position(self, data, index): # O(n)

        if (index < 0) or (index > self.size):
            raise ValueError("Índice Inválido!")

        if index == 0:
            self.insertion_at_beginning(data)

        elif index == self.size:
            self.insertion_at_end(data)

        else:

            node = Node(data)

            count = 1
            current = self.head

            while count < index:
                current = current.next
                count += 1

            node.next = current.next
            current.next = node

            self.size += 1


    def delete_from_beginning(self): # O(1)

        if self.size == 0:
            return

        if self.head.next == self.head:
            self.head = None

        else: 
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next

        self.size -= 1


    def delete_from_end(self): # O(n)

        if self.size == 1:
            self.head = None
            self.size = 0

        elif self.size > 1:

            current = self.head
            previous = None

            while current.next != self.head:
                previous = current
                current = current.next

            previous.next = self.head
            self.size -= 1

    def delete_at_position(self, index): # O(n)

        if (index < 0) or (index >= self.size):
            raise ValueError("Índice Inválido!") 

        if (index == 0):
            self.delete_from_beginning()

        elif index == (self.size-1):
            self.delete_from_end()

        else:

            current = self.head
            previous = None
            count = 0

            while count < index:
                previous = current
                current = current.next
                count += 1

            previous.next = current.next
            self.size -= 1

    def search(self, data):

        if self.head is None:

            return False

        current = self.head

        while True:

            if current.data == data:
                return True

            current = current.next

            if current == self.head:
                break

        return False