import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ex01 import imprimir_lista_encadeada
from singly_linked_list import SinglyLinkedList, Node

def organizar_lista(current: Node, k: int, head: Node, prev = None) -> Node:

    pass

    

if __name__ == '__main__':

    lista = SinglyLinkedList()
    lista.insertion_at_end(2)
    lista.insertion_at_end(8)
    lista.insertion_at_end(6)
    lista.insertion_at_end(7)
    lista.insertion_at_end(10)
    lista.insertion_at_end(11)

    head = organizar_lista(lista.head, 10, lista.head)

    imprimir_lista_encadeada(head)
