def swap_positions(input_list, position_1, position_2):
    # Just memorize it, the RHS is the same across the 3 equations. It's a no brainer.
    # And the LHS is 1-2-1. 3 equations to make your life easy.
    input_list[position_1] = input_list[position_1] ^ input_list[position_2]
    input_list[position_2] = input_list[position_1] ^ input_list[position_2]
    input_list[position_1] = input_list[position_1] ^ input_list[position_2]
    return input_list

print(swap_positions([1,2,3,4], 2,3))