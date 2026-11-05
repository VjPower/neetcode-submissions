class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        sol = []
        for i in range(0, len(nums)):
            # if nums[i] == nums[i-1] and i>0:
            #     continue

            l = i+1
            r = len(nums) - 1

            if r == i:
                r -=1
            if l == i:
                l +=1

            while l<r:
                if nums[l] + nums[r] > 0 - nums[i]:
                    r -=1
                elif nums[l] + nums[r] < 0 - nums[i]:
                    l +=1
                else:
                     if sorted([nums[i] , nums[l], nums[r]]) not in sol:
                         sol.append(sorted([nums[i] , nums[l], nums[r]]))
                     l +=1
                     r -=1
                
                if r == i:
                    r -=1
                if l == i:
                    l +=1

        return sol 