import sys
import os

from queue_linked_list import Queue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def delete_n_esimo_elemento(q: Queue, n, len_q):

    size = len_q

    for i in range(size):

        if i == n:
            q.dequeue()

        else:

            q.enqueue(q.dequeue())

    return q