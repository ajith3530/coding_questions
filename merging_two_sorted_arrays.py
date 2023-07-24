


import math


# using GAP method
def merge_sorted_arrays(input_array_1, input_array_2):
    window_size = math.ceil((len(input_array_1) + len(input_array_2))/2)
    input_array_1.extend(input_array_2)
    merged_array = input_array_1

    while True:
        low, high = 0, window_size
        while high < len(merged_array):
            if merged_array[low] > merged_array[high]:
                merged_array[low], merged_array[high] = merged_array[high], merged_array[low]
            # Iterate
            low += 1
            high = low + window_size
        if window_size == 1:
            break
        window_size = math.ceil(window_size/2)
    return merged_array

input_array_1 = [1,2,3,8,9]
input_array_2 = [4,5,6,7]
output = merge_sorted_arrays(input_array_1=input_array_1, input_array_2=input_array_2)
pass