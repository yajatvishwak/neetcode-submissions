class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d= {
            ']': '[',
            ')': '(',
            '}': '{'
        }
        for i in s:
            if i in '([{':
                stack.append(i)
            if i in ')}]':
                st = d[i]
                if not stack or stack.pop() != st:
                    return False
                
        return not stack
