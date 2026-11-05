class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for x in strs:
            l = len(x)
            s += "$"+str(l) + "$" +x

        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0

        while i<len(s):
            if s[i] == "$":
                i +=1
                t = ""
                while s[i]!="$":
                    t += s[i]
                    i +=1
                t = int(t)
                result.append(s[i+1:i+t+1])
                i = i+t+1

        return result