import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList

def remove_pares(lista: SinglyLinkedList) -> SinglyLinkedList: # O(n²)

    current = lista.head
    count = 0

    while current:

        if (current.data % 2) == 0:

            lista.delete_at_position(count)

        else:

            count += 1

        current = current.next

    return lista

def remove_pares2(lista: SinglyLinkedList) -> SinglyLinkedList: # O(n)

    while lista.head.data % 2 == 0 and lista.head:
        lista.head = lista.head.next

    if lista.head is None:
        return lista

    current = lista.head
    prev = None

    while current:

        if current.data % 2 == 0:
            current = current.next
            prev.next = current

        else:

            prev = current
            current = current.next

    return lista




if __name__ == "__main__":
    lista = SinglyLinkedList()
    lista.insertion_at_end(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(6)
    lista.insertion_at_end(13)
    lista.insertion_at_end(34)

    lista = remove_pares2(lista)

    current = lista.head

    while current:
        
        print(current.data)
        current = current.next