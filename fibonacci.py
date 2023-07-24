def print_fibonacci_using_list(count: int) -> list:
    fibonacci_list = [0, 1]
    for index in range(count + 1):
        current_sum = fibonacci_list[-2] + fibonacci_list[-1]
        fibonacci_list.append(current_sum)
    return fibonacci_list[1:]


def print_fibonacci_using_recursion(count: int) -> int:
    if count in [1, 2]:
        return 1
    if count < 0:
        return 0
    return print_fibonacci_using_recursion(count -1) + print_fibonacci_using_recursion(count-2)

# print(print_fibonacci_using_recursion(count=5))
for i in range(10):
    print(print_fibonacci_using_list(count=i))

