from collections import Counter 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        for i in dic.values():
            if i>1:
                return True 
        return False
        
        