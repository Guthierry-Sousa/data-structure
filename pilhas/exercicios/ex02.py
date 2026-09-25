import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stack import Stack

def remove_all(p: Stack):

    if p.is_empty():
        return

    p.pop()
    return remove_all(p)

if __name__ == "__main__":

    s = Stack()
    t = Stack()

    s.push(1)
    s.push(2)
    s.push(3)

    print(s.is_empty())

    remove_all(s)

    print(s.is_empty())