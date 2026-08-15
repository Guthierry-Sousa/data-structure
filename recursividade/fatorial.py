def fatorial_iterativo(n: int): # O(n) ou Theta(n)

    fat = 1

    for i in range(1, n+1): 

        fat *= i

    return fat


# A função fatorial executa n chamadas recursivas até atingir o caso base. 
# O custo em memória é proporcional ao número de chamadas empilhadas, ou seja, também O(n).

def fatorial_recursivo(n: int): # O(n)

    if n == 0:

        return 1

    return n * fatorial_recursivo(n-1)

if __name__ == "__main__":

    n = 5

    print(f"{n}! (iterativo) = {fatorial_iterativo(n)}")
    print(f"{n}! (recursivo) = {fatorial_recursivo(n)}")

