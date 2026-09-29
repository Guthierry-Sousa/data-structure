import sys
import os

from queue_linked_list import Queue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pilhas.stack import Stack

def inverter_k_primeiros_elementos(f: Queue, k: int, n: int) -> Queue:

    s = Stack()

    for _ in range(k):
        s.push(f.dequeue())

    while not s.is_empty():
        f.enqueue(s.pop())

    for _ in range(n - k):
        f.enqueue(f.dequeue())

    return f
