from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        results = defaultdict(list)

        for x in strs:
            count = [0] * 26
            for i in x:
                count[ord(i) - ord('a')] += 1
            results[tuple(count)].append(x)

        return list(results.values())

        
        