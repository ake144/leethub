class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub = 0
        if len(t) == 0 and len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        for i in range(len(t)):
            if sub <= len(s) - 1:
                if s[sub] == t[i]:
                    sub += 1
        return sub == len(s)

            
    
           
        
        
        