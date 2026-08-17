class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            l = len(i)
            s+= str(l)+"#"+i
        return s


    def decode(self, s: str) -> List[str]:
        strs = []
        p = 0
        while p < len(s):
            j = p
            while s[j] != "#":
                j+=1
            i = int(s[p:j])
            strs.append(s[j+1: j+i+1])
            p = i + 1 + j

        return strs
            
