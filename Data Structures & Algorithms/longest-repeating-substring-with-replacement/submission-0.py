class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = set()
        max_window_size = 0
        for r in range(len(s)):
            while len(window) > k:
                window.remove(s[l])
                l+=1
            max_window_size = max(max_window_size, r - l + 1)
            window.add(s[r])
        return max_window_size
            

        