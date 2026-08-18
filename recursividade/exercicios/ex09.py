def inverte(n: int, inverso: int) -> int:

    if n == 0:
        return inverso

    return inverte(n//10, (n%10)+10*inverso)

if __name__ == "__main__":
    n = 1234

    print((inverte(n, 0)))