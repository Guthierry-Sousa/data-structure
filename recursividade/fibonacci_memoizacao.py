# A recursão ingênua de Fibonacci (O(2^n)) é ineficiente por recalcular os mesmos valores.

# A técnica de memoização resolve isso armazenando cada resultado após o primeiro cálculo,
#  o que reduz a complexidade para O(n).

def fib_optimize(n: int):

    return fib_memo(n, dict_memo = dict())

def fib_memo(n: int, dict_memo: dict):

    if n <= 1:
        return n

    if n in dict_memo:
        return dict_memo[n]

    result = fib_memo(n-1, dict_memo) + fib_memo(n-2, dict_memo)
    dict_memo[n] = result

    return result

if __name__ == "__main__":

    n = 6

    print(f"{n}- elemento = {fib_optimize(n)}")
