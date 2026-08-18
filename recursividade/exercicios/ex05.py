def zera_pares(n: int) -> int:

    if n == 0:
        return 0

    a = n%10
    if a%2 == 0:
        a = 0

    return zera_pares(n//10) * 10 + a


if __name__ == "__main__":
    n = 123456

    print((zera_pares(n)))


    