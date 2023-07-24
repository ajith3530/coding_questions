def reverse_digits(input: int) -> int:
    """
    :param input:
    :return:
    """
    result, result_remaining = 0, input
    while result_remaining:
        result = result * 10 + result_remaining % 10
        result_remaining = result_remaining//10

    return result if input > 0 else -result


print(reverse_digits(123456))
