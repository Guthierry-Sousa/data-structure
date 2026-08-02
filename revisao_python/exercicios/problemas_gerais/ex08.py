# Leia números do usuário até que ele digite um valor inválido, exibindo uma mensagem amigável.

while True:

    try:

        n = float(input("Informe um número: "))

    except ValueError as e:

        print(f"Erro: {e}")
        break

    except Exception as e:

        print(f"Erro: {e}")
        break

    else:

        print(f"Número Digitado: {n}")

    

