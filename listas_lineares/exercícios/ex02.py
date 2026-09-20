import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList

def soma_impares(lista: SinglyLinkedList) -> int: # O(n)

    soma = 0

    current = lista.head

    while current:

        if current.data%2 != 0: # é impar
            soma += current.data

        current = current.next

    return soma


if __name__ == "__main__":
    lista = SinglyLinkedList()
    lista.insertion_at_end(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(6)
    lista.insertion_at_end(13)
    lista.insertion_at_end(34)

    print(soma_impares(lista))
