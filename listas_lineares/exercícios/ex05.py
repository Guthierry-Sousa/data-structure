import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList, Node

def n_esimo_elemento(head: Node, n: int, count = 0) -> int:

    if not head:
        return count, None

    count, result = n_esimo_elemento(head.next, n, count+1)
    count -= 1

    if count == n:
        return count, head.data

    return count, result

def n_esimo_elemento2(head: Node, n: int) -> int:

    if not head:
        return -1, None

    count, result = n_esimo_elemento(head.next, n)
    count += 1

    if count == n:
        return count, head.data

    return count, result

if __name__ == "__main__":
    lista = SinglyLinkedList()
    lista.insertion_at_end(1)
    lista.insertion_at_end(2)
    lista.insertion_at_end(6)
    lista.insertion_at_end(13)
    lista.insertion_at_end(34)

    _, data = n_esimo_elemento(lista.head, 0)
    print(data)

    