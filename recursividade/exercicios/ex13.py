def imprime_numeros(arr, idx):

    if idx == -1:
        return

    a = arr[idx]
    print(a)

    return imprime_numeros(arr, idx-1)

k = [1, 2, 3, 4, 5]
imprime_numeros(k, len(k) - 1)