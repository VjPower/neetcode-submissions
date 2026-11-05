class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(', '}':'{', ']':'['}
        queue = []
        length = 0
        x = 0

        while x<len(s):
            if s[x] in ('(', '{', '['):
                queue.append(s[x])
                length +=1
                x +=1
            else:
                while x<len(s) and s[x] in map:
                    if length > 0 and queue[length - 1] == map[s[x]]:
                        queue.pop()
                        x +=1
                        length -=1
                    else:
                        return False
                    
        if len(queue) != 0:
            return False
        return True 