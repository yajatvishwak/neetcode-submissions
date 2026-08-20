class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxx = 0
        for i in nums:
            if i - 1 in s:
                continue
            n = 1
            x = i
            while (x+1) in s:
                n+=1
                x +=1
            maxx = max(maxx, n)
        return maxx
                
        