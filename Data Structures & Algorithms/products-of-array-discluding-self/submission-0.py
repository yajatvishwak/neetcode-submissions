class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = [1]
        pre = 1
        for i in range(0, len(nums) - 1):
            pre *= nums[i]
            arr1.append(pre)
        arr2 = [1]
        suf = 1
        for i in range(len(nums) - 1, 0, -1):
            suf *= nums[i]
            arr2.append(suf)
        
        r = len(nums) - 1
        w = 0
        
        while w < len(nums):
            m = arr1[w] * arr2[r]
            arr1[w] = m
            w+=1
            r-=1
        return arr1
        