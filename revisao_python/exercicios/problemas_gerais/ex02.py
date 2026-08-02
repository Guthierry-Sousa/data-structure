# Receba uma lista de números inteiros e exiba a soma, o maior e o menor valor, e a média dos números.

import random as rd

def gerar_estatisticas_lista(lista: list):

    if not lista:

        raise ValueError("Erro: Lista Vazia")

    max_value = max(lista)
    min_value = min(lista)
    sum_total = sum(lista)
    qtd_elementos = len(lista)
    media = sum_total / qtd_elementos

    return (max_value, min_value, sum_total, media)

lista = [rd.randint(1, 100) for _ in range(10)]
print(lista)

try:

    maior, menor, soma, media = gerar_estatisticas_lista(lista)

except Exception as e:

    print(e)

else:

    print(f"Maior valor: {maior}")
    print(f"Menor valor: {menor}")
    print(f"Soma dos elementos: {soma}")
    print(f"Média dos elementos: {media:.2f}")

