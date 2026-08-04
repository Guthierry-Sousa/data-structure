def sum_quadrados_menores_que_n(n: int) -> int:

    soma = 0

    for i in range(1, n):

        soma += (i*i)

    return soma

def sum_quadrados_menores_que_n_2(n: int) -> int:

    return sum(i*i for i in range(1, n))

if __name__ == '__main__':
    n = int(input("Informe um número: "))
    result = sum_quadrados_menores_que_n_2(n)
    print(f"Soma = {result}")

