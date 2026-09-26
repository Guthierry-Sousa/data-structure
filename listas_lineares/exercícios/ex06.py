import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from listas_simplesmente_encadeadas.singly_linked_list import SinglyLinkedList, Node


def detect_loop(head: Node) -> bool:

    fast = low = head

    while fast.next is not None:

        fast = fast.next

        if fast.next is None:
            return False

        fast = fast.next
        low = low.next

        if fast == low:
            return True

    return False

if __name__ == "__main__":
    n5 = Node(5)
    n4 = Node(4); n4.next = n5
    n3 = Node(3); n3.next = n4
    n2 = Node(2); n2.next = n3
    n1 = Node(1); n1.next = n2

    print(detect_loop(n1))

    n4 = Node(4)
    n3 = Node(3); n3.next = n4
    n2 = Node(2); n2.next = n3
    n1 = Node(1); n1.next = n2

    print(detect_loop(n1))

    n5 = Node(5)
    n4 = Node(4); n4.next = n5
    n3 = Node(3); n3.next = n4
    n2 = Node(2); n2.next = n3
    n1 = Node(1); n1.next = n2
    n5.next = n2  

    print(detect_loop(n1))

    n1 = Node(1)
    n1.next = n1  

    print(detect_loop(n1))