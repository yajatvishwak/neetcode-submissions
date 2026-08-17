class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        x = Counter(s)
        y = Counter(t)
        return x == y
        