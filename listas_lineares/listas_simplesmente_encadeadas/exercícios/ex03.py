import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from singly_linked_list import SinglyLinkedList, Node

def imprime_impares(head: Node):

    if head is None:
        return

    if head.data % 2 != 0:
        print(head.data, end=' ')

    imprime_impares(head.next)

if __name__ == '__main__':

    lista = SinglyLinkedList()
    lista.insertion_at_end(2)
    lista.insertion_at_end(8)
    lista.insertion_at_end(6)
    lista.insertion_at_end(7)
    lista.insertion_at_end(10)
    lista.insertion_at_end(11)

    imprime_impares(lista.head)
