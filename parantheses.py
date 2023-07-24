"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

parantheses_lookup = {"[": 0,
                      "]": 0,
                      "(": 0,
                      ")": 0,
                      "{": 0,
                      "}": 0}

def update_lookup(value):
    search_value = parantheses_lookup.get(value)
    if search_value is not None:
        parantheses_lookup[value] = search_value + 1

def validate_lookup():
    if parantheses_lookup["["] == parantheses_lookup["]"] and\
            parantheses_lookup["("] == parantheses_lookup[")"] and\
            parantheses_lookup["{"] == parantheses_lookup["}"]:
        return True
    return False


def check_parantheses(input_string):
    for char in input_string:
        update_lookup(char)
    return validate_lookup()

print(check_parantheses("()[]{}[]{}"))
