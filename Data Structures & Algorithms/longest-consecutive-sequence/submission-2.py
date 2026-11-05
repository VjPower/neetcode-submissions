class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        l = 0
        if len(nums) == 0:
            return 0

        for i in range(0, len(nums)):
            temp_l = 0
            pointer = nums[i]

            if pointer + 1 in numset:
                continue

            while pointer - 1 in numset:
                temp_l +=1
                pointer -=1
            l = max(temp_l, l)

        return l+1