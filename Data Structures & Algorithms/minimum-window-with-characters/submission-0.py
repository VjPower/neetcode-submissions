class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        l = 0
        min_string = ""

        for i in range(0, len(s)):
            if s[i] in count_t:
                count_t[s[i]] -=1

            while max(count_t.values()) <= 0:

                if min_string == "":
                    min_string = s[l:i+1]
                else:
                    if len(min_string) > i-l+1:
                        min_string = s[l:i+1]
                
                if s[l] in count_t:
                    count_t[s[l]] +=1
                l+=1

        return min_string
        