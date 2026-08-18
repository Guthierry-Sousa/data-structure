def count_vogais(s: str) -> bool:

    vogais = ['a', 'e', 'i', 'o', 'u']

    if len(s) == 0:
        return 0

    if s[0].lower() in vogais:
        return 1 + count_vogais(s[1:])

    return count_vogais(s[1:])

def tem_mais_vogais(s: str):
    count = count_vogais(s)
    return count > (len(s) // 2)

if __name__ == "__main__":
    s1 = "abacaxiuo"
    s2 = "abc"

    print((tem_mais_vogais(s1)))
    print((tem_mais_vogais(s2)))