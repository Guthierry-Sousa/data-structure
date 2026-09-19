from stack import Stack

def check_brackets(expression):

    stack = Stack()

    for ch in expression:

        if ch in "([{":

            stack.push(ch)

        if ch in ")]}":

            last = stack.pop()

            if (last == '(') and (ch == ')'):
                continue

            elif (last == '[') and (ch == ']'):
                continue

            elif (last == '{') and (ch == '}'):
                continue

            else:

                return False

    if stack.is_empty():

        return True

    return False

if __name__ == '__main__':

    expression1 = "(a+b)*(a-b)"
    expression2 = "(a+b]-a"
    expression3 = "((a+b)+(c-d)"

    print(check_brackets(expression1))
    print(check_brackets(expression2))
    print(check_brackets(expression3))