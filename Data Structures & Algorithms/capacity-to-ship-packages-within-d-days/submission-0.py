class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        def func(capacity):
            totaldays = 0
            currentcap = 0
            for w in weights:
                if capacity < (currentcap + w):
                    totaldays += 1
                    currentcap = 0
                currentcap += w
            return totaldays < days
                

        
        while l<=r:
            mid = (l+r) // 2
            if func(mid):
                ans = mid
                r = mid -1
            else:
                l = mid + 1
        return ans
