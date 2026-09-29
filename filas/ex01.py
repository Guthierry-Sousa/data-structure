# Exibir itens na ordem inversa
import sys
import os

from queue_linked_list import Queue
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pilhas.stack import Stack

def exibir_inverso(fila: Queue):

    stack = Stack()

    while not fila.is_empty():
        stack.push(fila.dequeue())

    while not stack.is_empty():
        print(stack.pop())

def exibir_inverso2(no):

    if no is None:
        return

    exibir_inverso2(no.next)
    print(no.data)

if __name__ == "__main__":

    fila = Queue()
    fila.enqueue(3)
    fila.enqueue(2)
    fila.enqueue(1)

    #exibir_inverso(fila)
    exibir_inverso2(fila.start())