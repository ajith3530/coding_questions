class Solution:
    def permute(self, nums):
        result = []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            permutations = self.permute(nums)

            for permutation in permutations:
                permutation.append(n)
            result.extend(permutations)
            nums.append(n)
        return result

input_nums = [1,2,3]
print(Solution().permute(input_nums))