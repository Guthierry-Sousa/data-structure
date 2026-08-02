# Crie uma função que receba uma string e retorne a string invertida.

def inverter_string(string: str) -> str:

    return string[::-1]

string = "Guthy mito"
string2 = "Arara"

print(inverter_string(string))
print(inverter_string(string2))