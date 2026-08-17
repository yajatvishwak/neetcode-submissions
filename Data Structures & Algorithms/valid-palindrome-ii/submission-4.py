class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palin(m):
            return m == m[::-1]
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i+=1
                j-=1
            else:
                x = is_palin(s[i+1: j+1])
                y = is_palin(s[i: j])
                return x or y
        return True
        