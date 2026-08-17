class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        ans = []
        for _ in range(k):
            key = max(d, key=d.get)
            ans.append(key)
            del d[key]
        return ans

        

    
        
        