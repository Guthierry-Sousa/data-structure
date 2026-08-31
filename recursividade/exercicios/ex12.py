def imprime_impares(arr, idx = 0):

    if idx > (len(arr) - 1):
        return

    a = arr[idx]
    if a%2 != 0:
        print(a)

    return imprime_impares(arr, idx+1)

k = [1, 2, 3, 4, 5]
imprime_impares(k)