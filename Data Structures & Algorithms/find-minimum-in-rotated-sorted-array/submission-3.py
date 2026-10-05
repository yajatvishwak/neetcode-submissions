class Solution:
    def findMin(self, arr: List[int]) -> int:
        ans = -1
        l, r = 0, len(arr) - 1
        while l<=r:
            m = (l+r) // 2
            if arr[m] > arr[-1]:
                l = m+1
            else:
                ans = m
                r = m - 1
            
        return arr[ans]

