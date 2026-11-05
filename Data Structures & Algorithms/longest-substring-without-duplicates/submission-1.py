class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count = defaultdict(int)
        l = 0
        max_length = 0

        for i in range(0, len(s)):
            count[s[i]] += 1

            while count[s[i]] > 1:
                count[s[l]] -=1
                l +=1

            max_length = max(max_length, i-l)

        return max_length + 1