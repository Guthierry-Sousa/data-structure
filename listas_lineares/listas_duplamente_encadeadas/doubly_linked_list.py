from node import Node

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

        self.size = 0

    def insertion_at_beginning(self, data): #O(1)

        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def insertion_at_end(self, data): # O(1)

        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

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
            current = self.head
            previous = None
            count = 0

            while count < index:
                previous = current
                current = current.next
                
                count += 1

            node.next = current
            node.prev = previous
            current.prev = node
            previous.next = node

        self.size += 1

    def search(self, data):# O(n)

        current = self.head

        while current:

            if current.data == data:
                return True

            current = current.next

        return False

    def delete_from_beginning(self): # O(1)

        if self.head is None:
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        else:
            self.tail = None
            
        self.size -= 1
            

    def delete_from_end(self): # O(1)

        if self.head is None:
            return

        self.tail = self.tail.prev

        if self.tail is not None:
            self.tail.next = None

        else:
            self.head = None

        self.size -= 1

    def delete_at_position(self, index): # O(n)

        if (index < 0) or (index >= self.size):
            raise ValueError("Índice Inválido!")

        if index == 0:
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
            current.next.tail = previous

        self.size -1

        


        
            



