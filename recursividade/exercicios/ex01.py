def maior_digito(n: int) -> int:

    if n < 10:
        return n

    return max(maior_digito(n//10), maior_digito(n%10))

if __name__ == "__main__":
    n = 821

    print(maior_digito(n))