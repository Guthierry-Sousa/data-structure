# Implementação TAD Pilha

class Stack:

    def __init__(self):
        self.__stack = []

    def push(self, item):

        self.__stack.append(item) 

    def pop(self):

        if not self._is_empty():

            return self.__stack.pop() 

    def top(self):

        if not self._is_empty():
        
            return self.__stack[-1] 

    def length(self):

        return len(self.__stack) 

    def _is_empty(self):

        return (self.length() == 0)

    def __str__(self):
        return f"Pilha: {self.__stack}"


# Testes
stack = Stack()

stack.push(10)
stack.push(3)
stack.push(5)
stack.push(19)

print(stack)

stack.pop()

print(stack)

print(f"Elemento do topo = {stack.top()}")