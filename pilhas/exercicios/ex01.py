import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stack import Stack

def transferir_dados(s: Stack, t: Stack):

    while not s.is_empty():

        t.push(s.pop())

    return t

if __name__ == "__main__":

    s = Stack()
    t = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print(s.peek())

    t = transferir_dados(s, t)

    print(t.peek())