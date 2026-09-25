import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stack import Stack

def invert_array(arr):

    p = Stack()
    n = len(arr)

    for i in range(n):
        p.push(arr[i])

    for i in range(n):
        arr[i] = p.pop()

    return arr

if __name__ == "__main__":

    array = [1 ,2 ,3, 4, 5]
    print(array)

    array2 = invert_array(array)

    print(array2)