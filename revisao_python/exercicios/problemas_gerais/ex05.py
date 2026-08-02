# Implemente uma classe com atributos para nome, preço e quantidade, métodos para calcular o valor do estoque e exibir as informações.

class Produto:

    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def valor_total(self):

        return self.__quantidade * self.__preco

    def __str__(self):
        return f"Nome: {self.__nome}\nPreço: {self.__preco}\nQuantidade: {self.__quantidade}\nValor Total: {self.valor_total()}\n"


prod1 = Produto("Maçã", 5.75, 10)
prod2 = Produto("Caneta", 2.00, 37)

print(prod1)
print(prod2)
