# Given a 32 bit integer, fit a 8 bit integer into it.
def bit_shifting_overwrite(number, position, new_number):
    if position + 8 > 31:
        return number
    # Create the mask
    mask = ~(0xFF << position)
    number &= mask
    number = number | (new_number << position)
    return number



main_number = 0xFF_FF_FE
new_number = 0b00010000
position = 8
print(hex(bit_shifting_overwrite(number=main_number,
             position=position,
             new_number=new_number)))