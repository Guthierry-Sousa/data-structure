def fibonacci_iterativo(n: int) -> int: # O(n)

    ant = 0
    atual = 1

    for _ in range(n): 

        prox = atual + ant
        ant = atual
        atual = prox

    return ant


# Cada chamada da função cria duas chamadas adicionais (exceto no caso base), resultando em uma árvore de chamadas exponencial

# a função Fibonacci recursiva tem complexidade exponencial, tornando-a extremamente ineficiente para valores grandes de n
def fibonacci_recursivo(n: int) -> int: # O(2^n)

        if n <= 1:

            return n

        return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

if __name__ == "__main__":

    n = 6

    print(f"{n}- elemento (iterativo) = {fibonacci_iterativo(n)}")
    print(f"{n}- elemento (recursivo) = {fibonacci_recursivo(n)}")

