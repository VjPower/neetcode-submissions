class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = Counter(s1)
        count2 = Counter(s2[0:len(s1)])

        l = 0
        r = len(s1)

        if count1 == count2: 
            return True 
        
        while r<len(s2):
            count2[s2[l]] -=1
            count2[s2[r]] +=1

            l+=1
            r+=1

            if count1 == count2:
                return True 

        return False
            