class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = {}
        slow = 0
        if k == 0:
            return 0
        max_len = 0
        for fast in range(len(s)):
            if s[fast] in d:
                d[s[fast]] +=1
            else:
                while len(d) >= k:
                    d[s[slow]] -= 1
                    if d[s[slow]] == 0:
                        del d[s[slow]]
                    slow+=1
                d[s[fast]] = 1
            max_len = max(max_len, fast - slow +1 )
        return max_len
        