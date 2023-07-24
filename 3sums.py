class Solution:
    def threeSum(self, nums):
        nums.sort()
        lenght = len(nums)
        triplets = set()
        for index in range(len(nums)):
            sum_to_find = nums[index]
            low = index+1
            high = lenght-1
            # If the sum is less than 0, we need to increase the variable values so that we reach 0.
            # So that's why we do low+=1 so that we can increase the component, and vice versa with high.
            while low < high and low < lenght and high > 0:
                diff = sum_to_find + nums[low] + nums[high]
                if diff < 0:
                    low += 1
                elif diff > 0:
                    high -= 1
                else:
                    triplets.add((sum_to_find, nums[low], nums[high]))
                    low += 1
                    high -= 1
        return triplets






input_list = [3,0,-2,-1,1,2]
print(Solution().threeSum(input_list))
