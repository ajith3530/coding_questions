def productExceptSelf(nums):
    product = 1
    output_array = [1] * len(nums)
    for index in range(len(nums)):
        output_array[index] = product * nums[index]
        product = output_array[index]

    index = len(nums) - 1
    product = 1
    while True:
        if index == 0:
            output_array[index] = product
            break
        output_array[index] = output_array[index - 1] * product
        product = nums[index] * product
        index -= 1
    return output_array

print(productExceptSelf([1,2,3,4]))


