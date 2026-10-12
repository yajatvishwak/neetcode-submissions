class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key] = self.d.get(key, [[],[]])
        self.d[key][0].append(value)
        self.d[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if not (key in self.d):
            return ""
        timestamps = self.d[key][1]
        values = self.d[key][0]

        l = 0
        r = len(timestamps) - 1
        ans = -1
        while l <= r :
            mid = (l+r) // 2
            if timestamps[mid] > timestamp:
                r = mid - 1
                
            else:
                ans = mid
                l = mid + 1
        return values[ans] if ans != -1 else ""

        
        
