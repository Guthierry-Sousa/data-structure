def selection_sort_iterativo(arr: list) -> list: # O(n²)

    n = len(arr)

    for i in range(n):

        min = i

        for j in range(i+1, n):

            if arr[j] < arr[min]:
                min = j

        if min != i:
            arr[i], arr[min] = arr[min], arr[i]

# A cada chamada, o algoritmo busca o menor valor no subvetor restante e o coloca na posição correta.
def selection_sort_recursivo(arr: list, i: int = 0) -> list: # O(n²)

    min = i

    if  i >= len(arr) - 1:
        return

    for j in range(i + 1, len(arr)):

        if arr[j] < arr[min]:
            min = j

    if min != i:
        arr[i], arr[min] = arr[min], arr[i]

    selection_sort_recursivo(arr, i+1)

if __name__ == "__main__":

    import random as rd
    arr1 = [rd.randint(1, 100) for _ in range(15)]

    print(f"Array original = {arr1}")
    selection_sort_iterativo(arr1)
    print(f"Array ordenado (iterativo) = {arr1}")

    arr2 = [rd.randint(1, 100) for _ in range(15)]

    print(f"Array original = {arr2}")
    selection_sort_recursivo(arr2, 0)
    print(f"Array ordenado (recursivo) = {arr2}")