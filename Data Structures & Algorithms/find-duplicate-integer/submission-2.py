class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while nums[i] != i + 1:
                j = nums[i] - 1

                if nums[i] == nums[j]:
                    return nums[i]

                nums[i], nums[j] = nums[j], nums[i]