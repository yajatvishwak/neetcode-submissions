class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        d = {}
        slow = 0
        max_len = 0
        for fast in range(len(s)):
            if s[fast] in d:
                d[s[fast]] +=1
            else:
                if len(d) < 2:
                    d[s[fast]] = 1
                else:
                    while len(d) >= 2:
                        d[s[slow]] -= 1
                        if d[s[slow]] == 0:
                            del d[s[slow]]
                        slow+=1
                    d[s[fast]] = 1
            max_len = max(max_len, fast - slow +1 )
        return max_len
