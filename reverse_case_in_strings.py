input_string = "AdnfA"

def reverse_case(input_string):
    diff = ord("a") - ord("A")
    limit = ord("Z")

    output = ""
    for char in input_string:
        reverse_char = ""
        reverse_char = chr(ord(char) + diff) if ord(char) < limit else chr(ord(char) - diff)
        output = "".join([output, reverse_char ])
    return output

print(reverse_case(input_string=input_string))
