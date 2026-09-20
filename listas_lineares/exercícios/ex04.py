import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList

def concat_listas(lista1: SinglyLinkedList, lista2: SinglyLinkedList) -> SinglyLinkedList:

    lista = SinglyLinkedList()

    current1 = lista1.head
    current2 = lista2.head

    while (current1 is not None) or (current2 is not None):

        if current1 is not None:

            lista.insertion_at_end(current1.data)
            current1 = current1.next
                    

        if current2 is not None:

            lista.insertion_at_end(current2.data)
            current2 = current2.next

    return lista

if __name__ == "__main__":
    lista1 = SinglyLinkedList()
    lista1.insertion_at_end(1)
    lista1.insertion_at_end(2)

    lista2 = SinglyLinkedList()
    lista2.insertion_at_end(6)
    lista2.insertion_at_end(13)
    lista2.insertion_at_end(34)

    lista = concat_listas(lista1 , lista2)

    current = lista.head

    while current:
        
        print(current.data)
        current = current.next
