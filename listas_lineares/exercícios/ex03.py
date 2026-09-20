import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList
from listas_circulares.circular_list import CircularList

def double_circular_list(lista: SinglyLinkedList) -> tuple[CircularList, CircularList]:

    circ_list1 = CircularList()
    circ_list2 = CircularList()
    size_list = lista.size
    count = 0
    current = lista.head

    while count < size_list:

        if count < (size_list//2):
            circ_list1.insertion_at_beginning(current.data)

        else:
            circ_list2.insertion_at_beginning(current.data)

        current = current.next
        count += 1

    return (circ_list1, circ_list2)


if __name__ == "__main__":
    lista = SinglyLinkedList()
    lista.insertion_at_end(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(6)
    lista.insertion_at_end(13)
    lista.insertion_at_end(34)

    lista1 , lista2 = double_circular_list(lista)

        