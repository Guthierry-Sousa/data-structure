# Implemente uma função que receba duas listas e retorne os elementos que estão apenas em uma delas.
import random as rd


def filtrar_elementos_unicos(lista1: list, lista2: list) -> tuple[list, list]:

    set1 = set(lista1)
    set2 = set(lista2)

    return (set1 - set2), (set2 - set1)

lista1 = [rd.randint(1, 20) for _ in range(10)]
lista2 = [rd.randint(1, 20) for _ in range(10)]

unicos_lista1, unicos_lista2 = filtrar_elementos_unicos(lista1, lista2)

print(f"Lista 1: {lista1}")
print(f"Lista 2: {lista2}")
print(f"Lista únicos 1: {unicos_lista1}")
print(f"Lista únicos 2: {unicos_lista2}")