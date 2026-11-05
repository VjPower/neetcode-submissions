class Solution:
    def maxArea(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        max_area = 0

        while l<r:
            area = min(nums[l], nums[r]) * (r-l)
            max_area = max(max_area, area)

            if nums[l] > nums[r]:
                r -=1
            elif nums[l] < nums[r]:
                l +=1
            else:
                r -=1
                l +=1

        return max_area