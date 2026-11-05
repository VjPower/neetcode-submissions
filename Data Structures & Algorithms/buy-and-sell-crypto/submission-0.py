class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        m = 0
        max_profit = 0
        min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[m]:
                m = i

            max_profit = max(max_profit, nums[i] - nums[m])


        return max_profit