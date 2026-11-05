class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0 
            else:
                return -1
            
        l = 0 
        r = len(nums) - 1

        while l<r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 

        min_index = l

        l = 0
        r = len(nums) - 1

        while l<=r:
            mid = (l+r)//2
            m_mid = (mid + min_index) % len(nums)

            if nums[m_mid] > target:
                r = mid - 1
            elif nums[m_mid] < target:
                l = mid + 1
            else:
                return m_mid
            
        return -1 