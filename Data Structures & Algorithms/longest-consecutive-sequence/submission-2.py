class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxx = 0
        if len(nums) == 0:
            return maxx
        for i in s:
            if i - 1 in s:
                continue
            n = 1
            x = i
            while (x+1) in s:
                n+=1
                x +=1
            maxx = max(maxx, n)
        return maxx
                
        