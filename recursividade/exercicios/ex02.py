def menor_digito(n: int) -> int:

    if n < 10:
        return n

    return min(menor_digito(n//10), menor_digito(n%10))

if __name__ == "__main__":
    n = 21498324

    print(menor_digito(n))