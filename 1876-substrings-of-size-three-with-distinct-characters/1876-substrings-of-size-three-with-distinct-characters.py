class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        j = len(s)-1
        arr = 0
        
        while i <j:
            if len(list(set(s[i:i+3]))) == 3:
                arr  += 1
            
            i += 1
        return arr
        
        