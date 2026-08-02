def all_unique(*nums: float) -> bool:

    if not nums:

        raise ValueError("É necessário informar pelo menos um número.")

    return len(nums) == len(set(nums))


if __name__ == "__main__":

    try:
        

        result = all_unique(1,2,3)

    except ValueError as e:

        print(e)

    else:

        if result:

            print("Todos os números são diferentes entre si.")

        else:

            print("Existe pelo menos um número repetido")