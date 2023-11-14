# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r= n
        while l <= r:
            md = (r + l) // 2
            if guess(md) == 0:
                return md
            if guess(md)  == 1:
                l = md +1
            else:
                r = md -1
        return l
        
        
        