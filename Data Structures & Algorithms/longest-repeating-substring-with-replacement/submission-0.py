class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        max_length = 0

        for i in range(0, len(s)):
            count[s[i]] +=1

            while (i - l + 1) - max(count.values()) > k:
                count[s[l]] -=1
                l +=1

            max_length = max(i-l+1, max_length)

        return max_length