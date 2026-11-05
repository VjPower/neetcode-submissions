class Solution:
    def trap(self, nums: List[int]) -> int:
        left_max = [0] * len(nums)
        right_max = [0] * len(nums)

        total_water = 0

        if len(nums) == 1 or len(nums) == 2:
            return 0


        for i in range(1, len(nums)):
            left_max[i] = max(left_max[i-1], nums[i-1])

        for i in range(len(nums) - 2, -1, -1):
            right_max[i] = max(right_max[i+1], nums[i+1])

        for i in range(0, len(nums)):
            water = max(0 , min(left_max[i], right_max[i]) - nums[i])
            total_water += water

        return total_water