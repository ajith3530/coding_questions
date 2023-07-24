def count_number_of_set_bits(number):
    count = 0
    while number:
        number &= (number-1)
        count += 1
    return count


print(count_number_of_set_bits(0b1100001001))