class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = defaultdict(list)

        for i,v in count.items():
            bucket[v].append(i)

        result = []

        i = len(nums) + 1

        while len(result) < k:
            if i in bucket:
                result.extend(bucket[i])
            i -=1

        return result[:k]