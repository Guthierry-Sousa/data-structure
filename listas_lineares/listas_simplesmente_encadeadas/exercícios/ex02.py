import sys
import os

from ex01 import imprimir_lista_encadeada

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from singly_linked_list import SinglyLinkedList, Node

def remover_elementos_v(head: Node, v: int):

    prev = None
    current = head

    while current:

        if current.data == v:
            
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

if __name__ == '__main__':

    lista = SinglyLinkedList()
    lista.insertion_at_end(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(3)
    lista.insertion_at_end(3)
    lista.insertion_at_end(3)
    lista.insertion_at_end(3)
    lista.insertion_at_end(2)
    lista.insertion_at_end(2)
    lista.insertion_at_end(2)

    imprimir_lista_encadeada(lista.head)
    head = remover_elementos_v(lista.head, 1)
    print()
    imprimir_lista_encadeada(head)

