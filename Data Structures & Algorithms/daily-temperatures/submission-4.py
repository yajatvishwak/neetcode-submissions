class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures) 
        for index, temp  in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                p = stack.pop()
                res[p] = index - p        
            stack.append(index)
        return res
# time taken: 30+ mins
# forgot the monotonic stack concept. read about it after 20 mins and then saw the solution took another 15 mins to understand how it works, it finally clicked after dry running 2-3 times
# Hint: everytime we are asked to find next largest item in an array we use a stack
# Hint: every in this question we are trying to find distance between the hot temps thats why we store indexes in the stack
# Hint: store the hottest day you have seen so far, any cooler day gets added on, once we find a hotter day than the last coldest day we have seen, we start popping till the stacks top is cooler
        
        