import sys
import os

from queue_linked_list import Queue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pilhas.stack import Stack

q = Queue()

def push(data):
    q.enqueue(data)

def pop():

    n = q.size()
    data = None

    for i in range(n):

        data = q.dequeue()

        if i!=(n-1):
            q.enqueue(data)

    return data