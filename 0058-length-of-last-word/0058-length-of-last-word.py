class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_new = s.strip()
        lis = list(s_new.split(" "))
        print(lis)
        return len(lis[-1])
                
        