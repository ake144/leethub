class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        tot = 0
        n = len(nums)
        for i in range(len(nums)):
            if n % (i + 1)==0:
                tot += nums[i] * nums[i]
        return tot
            