
GLOBAL_TOKEN = 100
def generate_token():
    global GLOBAL_TOKEN
    current_token = GLOBAL_TOKEN + 1
    GLOBAL_TOKEN = current_token
    return current_token

print(generate_token())
print(generate_token())
print(generate_token())
print(generate_token())