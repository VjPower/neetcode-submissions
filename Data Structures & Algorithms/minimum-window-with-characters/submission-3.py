class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        l = 0
        min_string = ""

        requirement = 0
        for i in count_t.values():
            requirement +=i 

        for i in range(0, len(s)):
            if s[i] in count_t:
                count_t[s[i]] -=1
                if requirement >= 0 and count_t[s[i]]>=0:
                    requirement -=1

            while requirement == 0:
                if min_string == "":
                    min_string = s[l:i+1]
                else:
                    if len(min_string) > i-l+1:
                        min_string = s[l:i+1]

                if s[l] in count_t:
                    count_t[s[l]] +=1      
                    if count_t[s[l]] >0:
                        requirement +=1
                l +=1

        return min_string