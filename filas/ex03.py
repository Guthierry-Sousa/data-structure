import sys
import os

from queue_linked_list import Queue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pilhas.stack import Stack

def is_palindromo(word: str) -> bool:

    s = Stack()
    q = Queue()

    for c in word:
        s.push(c)
        q.enqueue(c)

    while (not s.is_empty()) and (not q.is_empty()):

        if s.pop() != q.dequeue():
            return False

    return True

if __name__ == "__main__":

    word1 = 'arara'
    word2 = 'ovo'
    word3 = 'guthy'

    print(is_palindromo(word1))
    print(is_palindromo(word2))
    print(is_palindromo(word3))