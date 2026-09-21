class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            start = i
            while len(stack) > 0 and stack[-1][0] > heights[i]:
                h,index = stack.pop()
                max_area = max(max_area, h * (i - index))
                start = index
            stack.append((heights[i],start))
        
        for h, index in stack:
            max_area = max(max_area, h * (len(heights) - index))
        return max_area