class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = {}
        for i in t:
            check[i] = check.get(i, 0)  + 1
        l = 0
        window = {}
        have = 0
        need = len(check)
        res = {"l": -1, "r": -1}
        resLen = float("infinity")
        for r in range(len(s)):
            charR = s[r]
            window[charR] = window.get(charR, 0) + 1
            if charR in check and check[charR] == window[charR]:
                have += 1
            while have == need:
                if resLen > (r-l+1):
                    res = {"l":l, "r":r}
                    resLen = r-l+1
                charL = s[l]
                window[charL] -= 1
                if charL in check and window[charL] < check[charL]:
                    have -= 1
                l+=1
        return s[res["l"]:res["r"] + 1] if resLen != float("infinity") else ""
        
            
        