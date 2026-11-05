class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        
        multiplier = 1
        rev_multiplier = 1

        for i in range(0, len(nums)):
            j = len(nums) - 1 - i

            result[i] *= multiplier
            result[j] *= rev_multiplier

            multiplier *= nums[i]
            rev_multiplier *= nums[j]

        return result