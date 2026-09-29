import sys
import os

from queue_linked_list import Queue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pilhas.stack import Stack

def dividir_fila_inverso(q: Queue, n: int):

    q1, q2 = Queue(), Queue()
    s = Stack()
    size = n

    while not q.is_empty():
        s.push(q.dequeue())

    count = 0

    while not s.is_empty():

        if count < (size//2):
            q2.enqueue(s.pop())

        else:
            q1.enqueue(s.pop())

        count += 1

    return q1, q2



    