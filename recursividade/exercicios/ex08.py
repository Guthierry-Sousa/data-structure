def remove_impares(n: int) -> int:

    if n == 0:
        return 0

    a = n%10
    if a%2 == 0:
        return remove_impares(n//10) * 10 + a

    return remove_impares(n//10)

if __name__ == "__main__":
    n = 123456789

    print((remove_impares(n)))