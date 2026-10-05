class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        def can_eat(speed):
            hours_taken = 0
            for p in piles:
                hours_taken += math.ceil(p/speed)
            return hours_taken <= h

        while l <= r:
            mid = (l+r) // 2
            if can_eat(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
        