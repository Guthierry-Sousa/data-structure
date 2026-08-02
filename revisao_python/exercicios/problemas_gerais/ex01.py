# Escreva um programa que leia o nome e a idade de uma pessoa e exiba uma mensagem formatada usando f-strings.

def imprimir_formatado(nome, idade):

    return f"Nome: {nome} | Idade: {idade}"

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

print(imprimir_formatado(nome, idade))