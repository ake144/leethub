# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            md = (r + l) // 2
            if isBadVersion(md) == True:
                r = md -1
            if isBadVersion(md) == False:
                l = md + 1
        return l
            
        