def conta_digitos(n: int) -> int:

    if n < 10:
        return 1

    return 1 + conta_digitos(n//10)

if __name__ == "__main__":
    n = 398

    print(conta_digitos(n))