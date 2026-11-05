class TimeMap:

    def __init__(self):
        self.l = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.l:
            self.l[key] = []

        self.l[key].append((timestamp, value)) 
    

    def get(self, key: str, timestamp: int) -> str:
        result = ""

        if key not in self.l:
            return ""

        l = 0 
        r = len(self.l[key]) - 1

        while l<=r:
            mid = (l+r)//2
            if timestamp < self.l[key][mid][0]:
                r = mid - 1
            elif timestamp > self.l[key][mid][0]:
                result = self.l[key][mid][1]
                l = mid + 1
            else:
                return self.l[key][mid][1]

        return result