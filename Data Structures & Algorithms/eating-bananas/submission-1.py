class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        k = float('inf')
        l = 0
        r = max(piles)

        temp_k = (l+r)//2
        while l<=r:
            i = 0
            time = 0
            for i in range(0, len(piles)):
                time += math.ceil((piles[i])/temp_k)

            if time<=h:
                k = min(k, temp_k)
                r = temp_k-1
            else:
                l = temp_k+1
            temp_k = max((l+r)//2,1)

        return k