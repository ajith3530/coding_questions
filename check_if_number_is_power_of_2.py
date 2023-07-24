def check_number_is_power_of_2(number):
    return not (number & (number-1))

print(check_number_is_power_of_2(64))