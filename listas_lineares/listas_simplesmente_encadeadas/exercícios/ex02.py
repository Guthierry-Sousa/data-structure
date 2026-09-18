import sys
import os

from ex01 import imprimir_lista_encadeada

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from singly_linked_list import SinglyLinkedList

def remover_elementos_v(lista: SinglyLinkedList, v: int):

    current = lista.head
    count = 0

    while current:

        if current.data == v:
            
            next_node = current.next
            lista.delete_at_position(count)
            current = next_node

        else:

            current = current.next
            count += 1

if __name__ == '__main__':

    lista = SinglyLinkedList()
    lista.insertion_at_beginning(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(3)
    lista.insertion_at_end(3)
    lista.insertion_at_end(3)
    lista.insertion_at_end(3)
    lista.insertion_at_end(2)
    lista.insertion_at_end(2)
    lista.insertion_at_end(2)

    imprimir_lista_encadeada(lista.head)
    remover_elementos_v(lista, 2)
    print()
    imprimir_lista_encadeada(lista.head)

