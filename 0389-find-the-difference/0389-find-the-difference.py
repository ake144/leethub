class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a = sorted(s)
        b = sorted(t)
        i = 0
        j =0
        while i < len(s) and j < len(t):
            if a[i] != b[j]:
                return b[j]
            i  += 1
            j += 1
        return b[-1]
        
        