
def isValid(s):
    lookup = {"[":"]",
             "{":"}",
              "(":")"}
    stack = []

    for char in s:
        if char in lookup:
            stack.append(char)
        elif len(stack) == 0 or lookup[stack.pop()] != char:
            return False

    return len(stack) == 0

print(isValid("({)}"))
