import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList, Node

def remove_pares(head: Node) -> Node: # O(n)

    prev = None
    current = head

    while current is not None:

        if current.data % 2 == 0:

            if current == head:
                current = current.next
                prev = current
                head = current

            else:
                prev.next = current.next
                current = current.next

        else:
            prev = current
            current = current.next

    return head

if __name__ == "__main__":
    lista = SinglyLinkedList()
    lista.insertion_at_end(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(6)
    lista.insertion_at_end(13)
    lista.insertion_at_end(34)

    head = remove_pares(lista.head)

    current = head

    while current:
        
        print(current.data)
        current = current.next