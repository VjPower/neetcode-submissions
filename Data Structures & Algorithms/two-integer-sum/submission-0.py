class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store= {}

        for i in range(0, len(nums)):
            complement = target - nums[i]

            if complement in store:
                return [store[complement], i]
            
            store[nums[i]]=i
        