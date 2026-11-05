class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        h = []
        heapq.heapify(h)
        output = []
        for i in range(len(nums)):
            l = i - k
            heapq.heappush(h, (-nums[i], i))
            while h[0][1] <= l:
                heapq.heappop(h)
            if i >= k - 1:
                output.append(-h[0][0])
        return output
        



        
        
        