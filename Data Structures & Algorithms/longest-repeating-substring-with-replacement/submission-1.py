class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_window_size = 0
        maxf = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l+=1
            max_window_size = max(max_window_size, r - l + 1)

        return max_window_size
            

        