from functools import reduce
def find_missing_number(input_list):
    input_list.extend(list(range(len(input_list)+1)))
    missing_number = reduce(lambda x, y: x^y, input_list )
    return missing_number

print(find_missing_number([1,2,0,4,5]))