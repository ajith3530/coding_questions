def convert_decimal2binary(number):
    remainder = 0
    binary_string = ""
    while number != 1 and number != 0:
        remainder_binary_equivalent = str(number % 2)
        number = number // 2
        binary_string = "".join([remainder_binary_equivalent, binary_string])
    binary_string = "".join([str(number), binary_string])
    return binary_string




print(convert_decimal2binary(0))
