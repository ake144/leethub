class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        b = set(nums)
        a = list(b)
        a.sort()
        print(a)
        if len(a) >= 3:
            return a[-3]
        else:
            return a[-1]
            
        