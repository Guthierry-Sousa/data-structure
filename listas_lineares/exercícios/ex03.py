import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList, Node
from listas_circulares.circular_list import CircularList

def double_circular_list(head: Node) -> tuple[Node, Node, Node]:

    fast = low = head

    while fast.next is not None:

        fast = fast.next
        if not fast.next:
            break

        fast = fast.next
        low = low.next

    fast.next = low.next
    low.next = head

    return head, fast.next


if __name__ == "__main__":
    lista = SinglyLinkedList()
    lista.insertion_at_end(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(6)
    lista.insertion_at_end(13)
    lista.insertion_at_end(34)

    start1, start2 = double_circular_list(lista.head)

    print('Lista 1: ')
    
    current = start1
    while current.next != start1:
        print(current.data)
        current = current.next
    print(current.data)

    print('Lista 2: ')
    current = start2
    while current.next != start2:
        print(current.data)
        current = current.next
    print(current.data)
        