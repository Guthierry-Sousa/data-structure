import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList, Node

def concat_listas(head1: Node, head2: Node) -> SinglyLinkedList:

    current1 = head1
    current2 = head2

    l = SinglyLinkedList()

    while (current1 is not None) or (current2 is not None):

        if current1 is not None:
            l.insertion_at_end(current1.data)
            current1 = current1.next

        if current2 is not None:
            l.insertion_at_end(current2.data)
            current2 = current2.next

    return l

if __name__ == "__main__":
    lista1 = SinglyLinkedList()
    lista1.insertion_at_end(1)
    lista1.insertion_at_end(2)
    lista1.insertion_at_end(3)

    lista2 = SinglyLinkedList()
    lista2.insertion_at_end(4)
    lista2.insertion_at_end(5)
    lista2.insertion_at_end(6)

    lista = concat_listas(lista1.head , lista2.head)

    current = lista.head

    while current:
        
        print(current.data)
        current = current.next
