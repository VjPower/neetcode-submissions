class Solution:
    def characterReplacement(self, s: str, k: int) -> int:        
        count = defaultdict(int)
        max_freq = 0

        l = 0
        window_max = 0

        for i in range(0, len(s)):
            count[s[i]] +=1
            max_freq = max(max_freq, count[s[i]])

            while (i-l+1) - max_freq  > k:
                count[s[l]] -= 1
                l +=1

            window_max = max(window_max, i-l+1)

        return window_max