def generator_function():
    input_list = [1,2,3,4]
    for element in input_list:
        yield element

for value in generator_function():
    print(value)