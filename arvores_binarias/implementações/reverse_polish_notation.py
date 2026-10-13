# Parsing de uma expressão polonesa reversa

from node import Node

class Stack:

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

def calc(root: Node):

    if root.data == '+':
        return calc(root.left_child) + calc(root.right_child)

    if root.data == '-':
        return calc(root.left_child) - calc(root.right_child)

    if root.data == '*':
        return calc(root.left_child) * calc(root.right_child)

    if root.data == '/':
        return calc(root.left_child) / calc(root.right_child)

    else:

        return root.data

def parsing_reverse_polish_notation(expr: str):

    stack = Stack()
    for c in expr:

        if c in "+-*/":

            root = Node(c)
            root.right_child = stack.pop()
            root.left_child = stack.pop()

            stack.push(root)

        else:

            stack.push(Node(float(c)))

    return stack.pop()

expr = '12+34-*' #Expressão pós-fixa

root = parsing_reverse_polish_notation(expr)
print(calc(root))

