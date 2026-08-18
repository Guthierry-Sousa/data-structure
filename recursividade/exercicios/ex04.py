def soma_digitos(n: int) -> int:

    if n < 10:
        return n

    return soma_digitos(n//10) + soma_digitos(n%10)

if __name__ == "__main__":
    n = 10

    print(soma_digitos(n))