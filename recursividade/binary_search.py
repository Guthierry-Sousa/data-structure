def binary_search_iterativa(arr: list, value) -> tuple[bool, int]: # O(log n)

    start = 0
    end = len(arr) - 1

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] == value:
            return True, mid

        if value > arr[mid]:
            start = mid + 1

        else: 
            end = mid - 1

    return False, None

def binary_search_recursiva(arr: list, value) -> int:

    if len(arr) == 0:
        return None

    mid = (len(arr) - 1) // 2

    if arr[mid] == value:
        return mid

    if value < arr[mid]:
        return binary_search_recursiva(arr[:mid], value)

    idx = binary_search_recursiva(arr[mid+1:], value)

    if idx is None:

        return idx

    return idx + mid + 1

def binary_search_recursiva2(arr: list, value, start, end) -> int:

    if (start > end):
        return None

    mid = (start + end) // 2

    if arr[mid] == value:
        return mid

    if value < arr[mid]:
        return binary_search_recursiva2(arr, value, start, mid - 1)

    return binary_search_recursiva2(arr, value, mid + 1, end)


if __name__ == "__main__":

    import random as rd
    from selection_sort import *

    arr = [rd.randint(1, 20) for _ in range(10)]

    print(f"Array = {arr}")

    # A busca binária necessita de um array ordenado
    selection_sort_recursivo(arr)
    print(f"Array Ordenado = {arr}")
    value = 10
    result, idx = binary_search_iterativa(arr, value)
    print(f"{value} está no array? {result} | Índice = {idx}")
    print(f"Índice (recursiva 1)= {binary_search_recursiva(arr, value)}")
    print(f"Índice (recursiva 2)= {binary_search_recursiva2(arr, value, 0, len(arr) - 1)}")