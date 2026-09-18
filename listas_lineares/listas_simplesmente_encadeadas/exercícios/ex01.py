import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from singly_linked_list import SinglyLinkedList

def imprimir_lista_encadeada(head):

    if head is None:
        return

    print(head.data, end=' ')
    imprimir_lista_encadeada(head.next)
    

if __name__ == '__main__':

    lista = SinglyLinkedList()
    lista.insertion_at_beginning(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(3)

    imprimir_lista_encadeada(lista.head)
