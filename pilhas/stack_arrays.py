class StackArray:

    def __init__(self, size):
        self.top = -1
        self.size = size
        self.__stack = [None for i in range(size)]

    def push(self, data):

        if (self.top+1) == self.size:
            raise IndexError("Stack Overflow!")

        self.top += 1
        self.__stack[self.top] = data


    def pop(self):

        if (self.top == -1):
            raise IndexError("Stack Underflow!")

        temp = self.__stack[self.top]
        self.__stack[self.top] = None
        self.top -= 1

        return temp

    def peek(self):

        if (self.top == -1):
            return None

        return self.__stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size-1


class StackArrayDynamic:

    def __init__(self, size: int = 10):
        self.size = size
        self.top = -1
        self.__stack = [None for _ in range(size)]

    def push(self, data):

        if (self.top + 1) == self.size:
            self.rezise(1)

        self.top += 1
        self.__stack[self.top] = data

    def pop(self):

        if (self.top == -1):
            raise IndexError("Stack Underflow!")

        temp = self.__stack[self.top]
        self.__stack[self.top] = None
        self.top -= 1

        if self.top+1 < (self.size // 2):
            self.rezise(2)

        return temp

    def rezise(self, dir):

        if dir == 1:

            self.size *= 2

        else:

            self.size = max(1, self.size // 2)
        
        new_stack = [None for _ in range(self.size)]

        for i in range(self.top+1):

                new_stack[i] = self.__stack[i]

        self.__stack = new_stack

    def peek(self):

        if (self.top == -1):
            return None

        return self.__stack[self.top]

    def is_empty(self):
        return self.top == -1


            

                


