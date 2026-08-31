def sum_impares(k:int):

    if k<10:
        if k%2 != 0:
            return k
        return 0

    return sum_impares(k//10) + sum_impares(k%10)

k = 12345
print(sum_impares(k=k))
