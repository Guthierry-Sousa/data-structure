def counts_caracteres(string: str) -> dict:

    dict_counts = {}

    for s in string.replace(" ", "").lower():

        if dict_counts.get(s, None):

            dict_counts[s] += 1

        else:

            dict_counts[s] = 1

    return dict_counts

dict_counts = counts_caracteres("Paralelepipedo")

for k ,v in dict_counts.items():

    print(f"Caractere: {k} | Quantidade: {v}")


        