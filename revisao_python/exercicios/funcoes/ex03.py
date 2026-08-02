def max_and_min(*nums: float) -> tuple[float, float]:

    if not nums:

        raise ValueError("É necessário informar pelo menos um número.")

    return min(nums), max(nums)


if __name__ == "__main__":

    try:
        

        min_value, max_value = max_and_min(2,3,4,5,1,2,10,6,7,10,8.9, 10.5, 10.01, -0.55, 3)

    except ValueError as e:

        print(e)

    else:

        print(f"Maior valor: {max_value}")
        print(f"Menor valor: {min_value}")


