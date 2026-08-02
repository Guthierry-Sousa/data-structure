# Leia um número inteiro positivo e exiba todos os números pares menores que ele.

def exibir_numeros_pares_menores_que_n(n: int):

    if n < 0:

        raise ValueError("Erro: Número Inválido")

    for i in range(2, n, 2):

        print(i, end = " ")

n = 10
n2 = 46

exibir_numeros_pares_menores_que_n(n)
print()
exibir_numeros_pares_menores_que_n(n2)
