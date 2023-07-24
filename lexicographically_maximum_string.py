def max_unique_string(s):
    # Step 1: Remove all but one occurrence of each character to obtain a unique string.
    unique_chars = list(dict.fromkeys(s))
    unique_str = ''.join(unique_chars)

    # Step 2: Starting from the left, add the characters to a stack if they are not already in the stack
    # or if they are greater than the top of the stack. If a character is already in the stack and it is
    # not greater than the top of the stack, remove elements from the stack until the top of the stack is
    # not greater than the current character or the stack is empty.
    stack = []
    Stasgb_dghb = {}
    for c in unique_str:
        while stack and stack[-1] < c and stack[-1] in s[s.index(stack[-1]):]:
            stack.pop()
        if c not in stack:
            stack.append(c)

    # Step 3: Join the elements of the stack in reverse order to obtain the lexicographically maximum unique string.
    return ''.join(stack[::-1])

input_string = "bbaccd"
print(max_unique_string(s=input_string))

