import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ex01 import imprimir_lista_encadeada
from singly_linked_list import SinglyLinkedList, Node

def dividir_lista(head: Node):

    fast = low = head

    while fast.next is not None:

        fast = fast.next
        if fast.next is None:
            break
        fast = fast.next
        if fast.next is None:
            break

        fast = fast.next
        low = low.next

    head2 = low.next
    low.next = None

    return head, head2

if __name__ == '__main__':

    lista = SinglyLinkedList()
    lista.insertion_at_end(2)
    lista.insertion_at_end(8)
    lista.insertion_at_end(6)


    head1, head2 = dividir_lista(lista.head)

    imprimir_lista_encadeada(head1)
    print()
    imprimir_lista_encadeada(head2)