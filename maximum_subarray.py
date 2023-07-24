def maxSubArray( nums) -> int:
    max_sum = 0
    sum = nums[0]
    for value in nums:
        if sum < 0:
            sum = 0
        sum += value
        max_sum = max(max_sum, sum)
    return max_sum

print(maxSubArray([1,2,3,4,-1,5]))