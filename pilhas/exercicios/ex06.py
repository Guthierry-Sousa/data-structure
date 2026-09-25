import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stack import Stack

def gerar_instrucoes(expr: str):

    instrucoes = []

    p = Stack()

    dict_op = {
        '+': 'AD',
        '*': 'ML',
        '-': 'SB',
        '/': 'DV'
    }

    idx = 0

    for c in expr:

        if c not in dict_op.keys():
            p.push(c)

        else:

            a = p.pop()
            b = p.pop()
            instrucoes.append(f'LD {b}')
            instrucoes.append(f'{dict_op[c]} {a}')
            instrucoes.append(f'ST TEMP_{idx+1}')
            p.push(f'TEMP_{idx+1}')
            idx += 1

    return "\n".join(instrucoes)

if __name__ == '__main__':

    expression = 'ABC*+DE-/'

    print(gerar_instrucoes(expression))

    
