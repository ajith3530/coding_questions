def two_sums_function(sum: int, input_list: list) -> list:
    lookup = {value: index for index, value in enumerate(input_list)}
    while input_list:
        current = input_list.pop()
        search_value = sum-current
        value = lookup.get(search_value)
        if value is not None:
            return current, search_value
    return None

# Time Complexity - O(n)

print(two_sums_function(29, [400, 233, 3,24,5,2]))


