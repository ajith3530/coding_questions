# Quick Sort Implementation

# def quick_sort(input_list,):
#     def swap_positions(swap_list, position_1, position_2):
#         if len(swap_list) > 1:
#             swap_list[position_1] = swap_list[position_1] ^ swap_list[position_2]
#             swap_list[position_2] = swap_list[position_1] ^ swap_list[position_2]
#             swap_list[position_1] = swap_list[position_1] ^ swap_list[position_2]
#
#     if len(input_list) <= 1:
#         return input_list
#
#     pivot_swap_position = -1
#     pivot = max(0 ,len(input_list) - 1)
#     index = 0
#
#     while len(input_list) > 1 and index != pivot:
#         if input_list[pivot] > input_list[index]:
#             pivot_swap_position += 1
#             # Avoid unnecessary swaps - This happens quite frequently
#             if pivot_swap_position != index:
#                 swap_positions(input_list, pivot_swap_position, index)
#         index += 1
#
#     # After the loop is done, swap the pivot
#     pivot_swap_position += 1
#     input_list = swap_positions(input_list, pivot_swap_position, pivot)
#
#     quick_sort(input_list[:pivot_swap_position])
#     quick_sort(input_list[pivot_swap_position+1:])
#
#     return input_list


def quick_sort(input_list, start=0, end=None):
    if end is None:
        end = len(input_list) - 1

    if len(input_list[start:end+1]) < 2:
        return input_list
    pivot = end
    index = start
    swap_position = start-1
    while index < end and len(input_list) > 1:
        if input_list[index] < input_list[pivot]:
            swap_position += 1
            if swap_position < len(input_list):
                input_list[index], input_list[swap_position] = input_list[swap_position], input_list[index]
        index += 1
    swap_position += 1
    if swap_position < len(input_list):
        input_list[swap_position], input_list[pivot] = input_list[pivot], input_list[swap_position]
        pivot = swap_position

    quick_sort(input_list, start=pivot+1, end=end)
    quick_sort(input_list, start=start, end=pivot-1)
    return input_list





input_arr = [5,3,1,2, 0]
input_arr = [5,4,3,2,1,0]
print(quick_sort(input_list=input_arr))
