def binary_search(input_list, element):
    position = None
    start = 0
    end = len(input_list) - 1
    for _ in range(len(input_list)//2):
        mid = (start+end)//2
        if input_list[mid] == element:
            return mid
        elif input_list[mid] > element:
            end = mid
        else:
            start = mid
    return position

print(binary_search(input_list=[1,2,3,4], element=4))